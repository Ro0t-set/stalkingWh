var webdriver =require('selenium-webdriver')
driver = new webdriver.Builder().forBrowser('chrome').build();
var term = require( 'terminal-kit' ).terminal ;

term.grabInput() ;

driver.get('http://web.whatsapp.com')

    .then(_ =>
        driver.findElement(By.title('name')).sendKeys('webdriver', Key.RETURN))


    .then(_ => driver.quit());
