const { error } = require('console');
const {createServer} = require('http');
const methods = Object.create(null);
const {createReadStream, createWriteStream} = require("fs");
const {stat, readdir, mkdir, rmdir, unlink} = require("fs").promises;
const mime = require("mime");
const {parse} = require("url");
const {resolve, sep} = require("path");
const baseDirectory = process.cwd();


createServer((request, response) => {
    let handler = methods[request.method] || notAllowed;
    handler(request)
        .catch(error => {
            if (error.status != null) return error;
            else return {body: String(error), status: 500};
        })
        .then(({body, status = 200, type = "text/plain"}) => {
            response.writeHead(status, {"Content-Type": type});
            if (body && body.pipe) body.pipe(response);
            else response.end(body);
       });




}).listen(8000);


async function notAllowed(request) {
    return {
        status: 405,
        body: `Method ${request.method} not allowed.`
    };
}


methods.GET = async function(request) {
    let path = urlPath(request.url);
    let stats;
    try {
        stats = await stat(path);
    } catch (error) {
        if (error.code != "ENOENT") throw error;
        else return {status: 404, body: "File not found"};
    }

    if (stats.isDirectory()) {
        return {body: (await readdir(path)).join("\n")};
    } else {
        return {body: createReadStream(path),
                type: mime.getType(path)};
    }
};


methods.DELETE = async function(request) {
    let path = urlPath(request.url);
    let stats;
    try {
        stats = await stat(path);
    } catch (error) {
        if (error.code != "ENOENT") throw error;
        else return {status: 204};
    }

    if (stats.isDirectory()) await rmdir(path);
    else await unlink(path);
    return {status: 204};
};

function pipeStream(from, to) {
    return new Promise((resolve, reject) => {
        from.on("error", reject);
        to.on("error", reject);
        to.on("finish", resolve);
        from.pipe(to);
    })
}

methods.PUT = async function(request) {
    let path = urlPath(request.url);
    await pipeStream(request, createWriteStream(path));
    return {status: 204}; 
};

methods.MKDIR = async function(request) {

    let path = urlPath(request.url);
    try {
        await mkdir(path, {recursive: true});
        return {status: 204};
    } catch (error){
        console.error(error)
        return {status: 500, body: error};
    }
}

function urlPath(url) {
    let {pathname} = parse(url);
    let path = resolve(decodeURIComponent(pathname).slice(1));
    if (path != baseDirectory && !path.startsWith(baseDirectory + sep)) {
        throw {status: 403, body: "Forbidden"};
    }
    return path;
}