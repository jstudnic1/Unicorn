let user = {
	name: "John",
	value: "Doe",
	languages: ["en", "cs"]
  };

  let stringified = JSON.stringify(user);
  console.log(stringified);

  let newObject = JSON.parse(stringified);
  console.log(newObject);
