import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

client.hset('HolbertonSchools', 'Portland', 50, redis.print);

const KEY = 'HolbertonSchools';

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];

const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, index) => {
  client.hset(KEY, key, values[index], redis.print);
});

client.hgetall(KEY, (error, value) => {
  if (error) {
    console.error(error.message);
  } else {
    console.log(value);
  }
});
