const exp = require('constants');
const { test, expect } = require('./my-setup');

test('load webpage', async ({ webApp }) => {
    expect(webApp.locator('.login_logo'));
});

// Login Failure attempts
[
    { name: 'No login inputs', in_user: '', in_pass: '', err: 'Epic sadface: Username is required' },
    { name: 'Incorrect Password Login', in_user: process.env.STANDARD_USER, in_pass: "WRONG_PASS", err: 'Epic sadface: Username and password do not match any user in this service' },
    { name: 'Incorrect Username Login', in_user: 'WRONG_USER', in_pass: process.env.PASSWORD, err: 'Epic sadface: Username and password do not match any user in this service' }
].forEach(({name, in_user, in_pass, err}) =>{
    test(`${name}`, async ({ webApp }) => {
        // Check Username input is editable and enter Correct username
        expect(webApp.locator('input#user-name')).toBeEditable(true, 5000);
        await webApp.locator('input#user-name').fill(in_user);
        // Check password input is editable and enter incorrect password;
        expect(webApp.locator('input#password')).toBeEditable(true, 5000);
        await webApp.locator('input#password').fill(in_pass);

        //Login
        await webApp.locator('#login-button').click()
        //Confirm Error message
        expect(await webApp.locator('div.error-message-container.error h3')).toBeVisible()
        expect(await webApp.innerText('div.error-message-container.error h3')).toBe(err)
        expect(await webApp.locator('div.error-message-container.error h3 button.error-button'))
        //Confirm Username failure indicators
        expect(webApp.locator('input.input_error.form_input.error#user-name')) //Confrims red underline
        expect(webApp.locator('div svg.svg-inline--fa.fa-times-circle.fa-w-16.error_icon').first()) //Confirms X icon
        //Confirm Password failure indicators
        expect(webApp.locator('input.input_error.form_input.error#password')) //Confrims red underline
        expect(webApp.locator('div svg.svg-inline--fa.fa-times-circle.fa-w-16.error_icon').last()) //Confirms X icon
    });
});

test('Successful standard login', async ({ webApp }) => {
    expect(await webApp.locator('input#user-name')).toBeEditable(true, 5000);
    expect(await webApp.locator('input#password')).toBeEditable(true, 5000);

    await webApp.locator('input#user-name').fill(process.env.STANDARD_USER);
    await webApp.locator('input#password').fill(process.env.PASSWORD);
    await webApp.locator('input#login-button').click();

    const isloggedin = await webApp.locator('[data-test="title"]').textContent();
    expect(isloggedin).toContain('Products');
});

test('Logout', async ({ webApp }) => {
    // Login
    await webApp.locator('input#user-name').fill(process.env.STANDARD_USER);
    await webApp.locator('input#password').fill(process.env.PASSWORD);
    await webApp.locator('input#login-button').click();

    // Confirm login
    const isloggedin = await webApp.locator('[data-test="title"]').textContent();
    expect(isloggedin).toContain('Products');

    //logout
    await webApp.locator('#react-burger-menu-btn').click();
    await webApp.locator('.bm-item-list a#logout_sidebar_link').click();

    await webApp.locator('input#login-button').isVisible();
    // expect(webApp.locator('input#login-button')).isVisible();
});