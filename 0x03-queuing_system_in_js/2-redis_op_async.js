// import redis client
import redis from 'redis';
// Imports the promisify function from the Node.js util module.
import {promisify} from 'util';

// create a redis client
const client = redis.createClient();

// Converts the callback-based client.get method into a promise-based function.
const getAsync = promisify(client.get).bind(client);

// event handler for successfull connection
client.on('connect', () => (console.log('Redis client connected to the server')) );

// event handler for un-successfull connection
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

// Defines a function to set a new school name and value using the client.set method.
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Defines an asynchronous function to display the value of a
// 	school name using getAsync with await.
async function displaySchoolValue(schoolName) {
  // handles any errors that might occur during the asynchronous operation.
  try {
    const response = await getAsync(schoolName);
    console.log(response);
  } catch (error) {
    throw new Error(error);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
