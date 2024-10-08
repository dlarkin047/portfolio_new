const { test, expect } = require('@playwright/test')

const main_url = 'https://www.saucedemo.com/'
const std_user = 'standard_user'
const password = 'secret_sauce'
const wrong_pass = 'secret_sauce_fake'

exports.expect = expect;
exports.test = test.extend({
    webApp: async({ page }, use ) => {
        await page.goto(main_url)
        await page.getByText('Swag Labs').click();
        await use(page)
    },
    userStdLoggedIn: async({ webApp }, use) => {
        await webApp.locator('[data-test="username"]').fill(std_user)
        await webApp.locator('[data-test="password"]').fill(password)
        await webApp.locator('[data-test="login-button"]').click()
        await webApp.waitForURL(main_url+'inventory.html')
        await use(webApp)
        
    }
})