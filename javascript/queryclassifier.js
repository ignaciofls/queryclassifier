const { TextAnalyticsClient, AzureKeyCredential } = require("@azure/ai-text-analytics");
const key = 'x';
const endpoint = 'https://y.api.cognitive.microsoft.com/';
const textAnalyticsClient = new TextAnalyticsClient(endpoint, new AzureKeyCredential(key));
const query = ["How to refer a new employee for an open position"];

console.log("Query term is:", query);
if (query[0].split(" ").length>2) {
    console.log("This is a semantic query");
    languageDetection(textAnalyticsClient, query);
}
else {
    console.log("This is a syntax query");
}
 
async function languageDetection(client,queryterm) {
    const languageResult = await client.detectLanguage(queryterm);
    languageResult.forEach(document => {
        console.log(`\tPrimary Language ${document.primaryLanguage.name}`)
    });
}