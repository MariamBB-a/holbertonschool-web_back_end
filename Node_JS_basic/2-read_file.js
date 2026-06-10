const fields = {};

students.forEach((student) => {
  const parts = student.split(',');
  const firstname = parts[0];
  const field = parts[3];

  if (!fields[field]) {
    fields[field] = [];
  }

  fields[field].push(firstname);
});

Object.keys(fields).forEach((field) => {
  console.log(
    `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`,
  );
});
