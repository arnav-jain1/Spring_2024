/*

Author: Arnav Jain
Date: 3/19/23
Name: EECS 468 Assignment 6
Description: Server
Inputs: Various HTTP requests
Outputs: A file server
Collaborators: Just me and the slides that were provided 



Testing code: 
MKCOL: curl -X MKCOL http://localhost:8000/new-folder/test/
    This test is great because not only does it test to see if a new folder can be made, but it also tests whether it is possible to make multiple directories at once.
    The result was the creation of two new folders called new-folder and test inside of new-folder.
DELETE: curl -X DELETE http://localhost:8000/new-folder/test/
    This tests whether it is possible to delete a folder and whether it can distinguish between a file and a folder.
    The result was the deletion of the folder test inside of new-folder.
PUT: curl -X PUT -d "Hello, world!" http://localhost:8000/new-folder/hello.txt
    This tests whether it is possible to create a new file and write to it even if the file does not exist or is in a folder.
    The result was the creation of a new file called hello.txt with the contents "Hello, world!" inside of new-folder.
GET: curl -X GET http://localhost:8000/new-folder/hello.txt
    This tests whether it is possible to read the contents of a file and whether it can distinguish between a file and a folder.
    The result was the contents of the file hello.txt inside of new-folder (Hello, world!)
GET: curl -X GET http://localhost:8000/new-folder/
    This tests whether it is possible to read the contents of a folder and whether it can distinguish between a file and a folder.
    The result was the contents of the folder new-folder (hello.txt)
DELETE: curl -X DELETE http://localhost:8000/new-folder/hello.txt
    This tests whether it is possible to delete a file and whether it can distinguish between a file and a folder.
    The result was the deletion of the file hello.txt inside of new-folder.
INVALID: curl -X POST http://localhost:8000/new-folder/hello.txt
    This tests whether it is possible to distinguish between a valid and invalid request method.
    The result was the status 405 and the message "Method POST not allowed."
GET: curl http://localhost:8000/notthere.txt
    This tests whether the program can handle a file not being found.
    The result is the status 404 and the message "File not found."
DELETE: curl -X DELETE http://localhost:8000/notthere.txt
    This tests whether delete part of the program can handle a file not being found.
    The result is the status 404 and the message "File not found."


REPLIT: https://replit.com/join/enunqamvla-arnavjain71
*/



// Imports
import { error } from "console";
import { createServer } from "http";
import { createReadStream, createWriteStream } from "fs";
import { stat, readdir, mkdir, rmdir, unlink } from "fs/promises";
import mime from "mime";
import { parse } from "url";
import { resolve, sep } from "path";

// Methods object which is null and baseDirectory is the current working directory
const methods = Object.create(null);
const baseDirectory = process.cwd();

// Create a server and listen on port 8000
createServer((request, response) => {
    // Handler function which takes the request and returns the response. It triggers the notAllowed function if the method is not allowed
    let handler = methods[request.method] || notAllowed;
    //  The handler function is called
    handler(request)
    // If there is an error, catch it and return the error status and body as well as status 500
    .catch((error) => {
        if (error.status != null) return error;
        else return { body: String(error), status: 500 };
    })
    // If there is no error, then
    .then(({ body, status = 200, type = "text/plain" }) => {
        // Send the reponse with the status (200), type, and body
        response.writeHead(status, { "Content-Type": type });
        // If the body is a readable stream pipe it to the writeable response otherwise end the response
        if (body && body.pipe) body.pipe(response);
        else response.end(body);
    });
// Listen on port 8000
}).listen(8000);

// Function to handle any not allowed request methods (EX POST)
async function notAllowed(request) {
    // Return the status 405 and the message "Method not allowed" with the method name
    return {
        status: 405,
        body: `Method ${request.method} not allowed.`,
    };
}


// GET request method
methods.GET = async function (request) {
    // get the path from the url
    let path = urlPath(request.url);
    let stats;
    try {
        //  Get the information of the path and store it in the stats variable
        stats = await stat(path);
    } catch (error) {
        // If there is an error, check if the error code is ENOENT (file not found) and return 404 status and "File not found" body. If it is not ENOENT, throw the error
        if (error.code != "ENOENT") throw error;
        else return { status: 404, body: "File not found" };
    }

    //   If the stats are a directory, return the body as the directory contents joined by a new line
    if (stats.isDirectory()) {
        return { body: (await readdir(path)).join("\n") };
    } else {
        // Otherwise, return the body as a readable stream and the type as the mime type of the path
        return { body: createReadStream(path), type: mime.getType(path) };
    }
};

// DELETE request method
methods.DELETE = async function (request) {
    // Get the path from the url
    let path = urlPath(request.url);
    let stats;
    try {
        // Get the information of the path and store it in the stats variable
        stats = await stat(path);
    } catch (error) {
        // If there is an error, check if the error code is ENOENT (file not found) and return 404 status. If it is not ENOENT, throw the error
        if (error.code != "ENOENT") throw error;
        else return { status: 404, body: "File not found"};
    }

    // If the stats are a directory, remove the directory. Otherwise, unlink the file (which deletes the file)
    if (stats.isDirectory()) await rmdir(path);
    else await unlink(path);
    // return the status 204
    return { status: 204 };
};

// pipeStream function which takes a readable stream and a writeable stream and returns a promise
function pipeStream(from, to) {
    return new Promise((resolve, reject) => {
        // listen for an error on the from and to streams and resolve the promise when the to stream is finished
        from.on("error", reject);
        to.on("error", reject);
        to.on("finish", resolve);
        // Pipe the from stream to the to stream
        from.pipe(to);
    });
}

// Put request method
methods.PUT = async function (request) {
    // Get the path from the url
    let path = urlPath(request.url);
    // Pipe the request to a writeable stream 
    await pipeStream(request, createWriteStream(path));
    // Return the status 204
    return { status: 204 };
};

// MKCOL (make directory) request method
methods.MKCOL = async function (request) {
//   Get the path
    let path = urlPath(request.url);
    try {
        // Make the directory at the path (recursive is set to true so that it creates the directory and any parent directories if they do not exist)
        await mkdir(path, { recursive: true });
        // return 204 status
        return { status: 204 };
    } catch (error) {
        // If there is an error, return the error and status 500
        console.error(error);
        return { status: 500, body: error };
    }
};

// Helper func to get the path from the url
function urlPath(url) {
    //  pathname variable is set to the pathname of the url (parse function returns an object with the pathname property) 
    let { pathname } = parse(url);
    //   path variable is set to the resolved path of the pathname, decoded and sliced by 1 (to remove the / at the start)
    let path = resolve(decodeURIComponent(pathname).slice(1));
    //   IF the path is not the base directory and does not start with the base directory and a /, throw an error with status 403 and body "Forbidden"
    if (path != baseDirectory && !path.startsWith(baseDirectory + sep)) {
        throw { status: 403, body: "Forbidden" };
    }
    //   Return the path
    return path;
}