const axios = require('axios');
const cheerio = require('cheerio');

async function scrapeCzechMaleNames() {
  try {
    // Fetch HTML content from Wikipedia page containing Czech male names
    const response = await axios.get('https://cs.wikipedia.org/wiki/Seznam_nej%C4%8Dast%C4%9Bj%C5%A1%C3%ADch_mu%C5%BEsk%C3%BDch_jmen');
    const html = response.data;

    // Use Cheerio to load HTML content
    const $ = cheerio.load(html);

    // Select the relevant section containing Czech male names
    const sectionSelector = 'span#Nejčastější_mužská_jména_v_Česku';
    const section = $(sectionSelector);

    // Extract names from the section
    const names = [];
    section.find('li').each((index, element) => {
      const name = $(element).text().trim();
      names.push(name);
    });

    // Print the first 50 names
    console.log(names.slice(0, 50));

  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Run the web scraping function
scrapeCzechMaleNames();
