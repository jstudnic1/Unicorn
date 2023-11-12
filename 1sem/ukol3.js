function getRandomItem(array) {
	return array[Math.floor(Math.random() * array.length)]
}
function getRandomGender() {
	return Math.random() < 0.5 ? "male" : "female";
}

function getRandomWorkload() {
	const workload = [10,20,30,40];
	return getRandomItem(workload);
}

function getRandomInt(min, max) {
	return min + Math.floor(Math.random() * (max - min + 1));
}

function getRandomBirthdate(min, max) {
	const currentYear = new Date().getFullYear();
	const minYear = currentYear - max;
	const maxYear = currentYear - min + 1;

	const randomYear = getRandomInt(minYear, maxYear);
	const randomMonth = getRandomInt(1, 12);
	const randomDay = getRandomInt(1, 28);

	return new Date(randomYear, randomMonth - 1, randomDay).toISOString();
}

function getRandomEmployee (gender, age) {
	const maleNames = ["Jakub", "Tomas", "Matej", "Jan", "David", "Martin", "Lukas", "Filip", "Adam", "Vojtech", "Jiri", "Karel", "Michal", "Petr", "Pavel", "Ondrej", "Dominik", "Daniel", "Jakob", "Marek", "Oscar", "Antonin", "Radek", "Rudolf", "Viktor", "Josef", "Benjamin", "Patrik", "Svatoslav", "Tadeas", "Libor", "Miroslav", "Vladimir", "Stanislav", "Eduard", "Igor", "Robert", "Jaroslav", "Hugo", "Dalibor", "Bohumil", "Richard", "Oliver", "Sebastian", "Alan", "Ladislav", "Ales"];
	const femaleNames = ["Adéla", "Barbora", "Cecílie", "Denisa", "Eliška", "Františka", "Gabriela", "Hana", "Irena", "Jana", "Karolína", "Lucie", "Magdaléna", "Nela", "Olga", "Petra", "Radka", "Šárka", "Tereza", "Uršula", "Věra", "Wanda", "Xénie", "Yvona", "Zdeňka", "Alena", "Božena", "Čestmíra", "Diana", "Emílie", "Flóra", "Gita", "Helena", "Iva", "Jitka", "Klára", "Lenka", "Marie", "Natálie", "Otilie", "Pavlína", "Qiana", "Renáta", "Simona", "Tamara", "Urszula", "Vlasta", "Wlasta"];
	const maleSurnames = ["Novák", "Svoboda", "Novotný", "Dvořák", "Černý", "Procházka", "Kučera", "Veselý", "Horák", "Němec", "Pospíšil", "Marek", "Hájek", "Král", "Janda", "Jelínek", "Kříž", "Vlček", "Bartoš", "Polák", "Bílý", "Toman", "Štěpánek", "Dušek", "Fiala", "Růžička", "Pavelka", "Kolář", "Čech", "Bureš", "Urban", "Havel", "Kopecký", "Hruška", "Konečný", "Petržela", "Vávra", "Havlíček", "Holub", "Šimůnek", "Tomášek", "Koudelka", "Blažek", "Matoušek", "Linhart", "Moravec", "Kadlec"];
	const femaleSurnames = ["Kerdová", "Novotná","Nováková", "Svobodová", "Dvořáková", "Černá", "Procházková", "Kučerová", "Veselá", "Horáková", "Bartošová", "Marešová", "Kratochvílová", "Němcová", "Štěpánová", "Hájková", "Růžičková", "Pospíšilová", "Šimonová", "Kolářová", "Urbanová", "Bláhová", "Fialová", "Zemanová", "Richterová", "Křížová", "Dušková", "Holubová", "Benešová", "Jarošová", "Kopecká", "Machová", "Fialová", "Blažková", "Havlová", "Vlčková", "Jelínková", "Koubková", "Tichá", "Kasalová", "Vrbová", "Moravcová", "Sýkorová", "Pospíchalová", "Dlouhá", "Zábranská", "Burešová", "Sedláčková", "Váchová", "Jílková"];

	const birthday = getRandomBirthdate(age.min, age.max);
	const nameArray = gender === "male" ? maleNames : femaleNames;
	const surnameArray = gender === "male" ? maleSurnames : femaleSurnames;

	return {gender, birthday, name: getRandomItem(nameArray), surname: getRandomItem(surnameArray), workload: getRandomWorkload() };
}

function main(dtoIn) {
	const { count, age } = dtoIn;
	return Array.from({ length: count }, () => getRandomEmployee(getRandomGender(), age));
}

const dtoIn = {
	count: 50,
	age: {
	  min: 19,
	  max: 35
	}
};

const dtoOut = main(dtoIn);
console.log(dtoOut);
