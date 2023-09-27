import redis from 'redis';
const { promisify } = require('util');


const client = redis.createClient();

client.on('error', err => console.log('Redis client not connected to the server: ', err));
client.on('connect', () => console.log('Redis client connected to the server'));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (error, reply) => {
    if (error) console.error('Error: ', error);
    else {
      redis.print(`Reply: ${reply}`);
    }
  });
}

const getAsync = promisify(client.get).bind(client);

const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (error) {
    console.error(error);
  };
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

