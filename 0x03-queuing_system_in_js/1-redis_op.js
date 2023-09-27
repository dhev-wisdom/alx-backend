import redis from 'redis';


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

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (error, value) => {
    if (error) console.error('Error: ', error);
    else console.log(value);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

