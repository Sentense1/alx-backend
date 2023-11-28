// import redis client
import redis from 'redis';

// create a redis client
const client = redis.createClient();

// event handler for successfull connection
client.on('connect', () => (console.log('Redis client connected to the server')) );

// event handler for un-successfull connection
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

module.exports = function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

module.exports = function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, response) => {
    if (error) {
      throw new Error(error);
    } else {
      console.log(response);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');