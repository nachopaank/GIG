Feature: Challenge

  Scenario: TEST 1
    When I request user data
    Then Response is 200
    And The user list has at least 1 user

  Scenario: TEST 2
    When I request user data
    Then Response is 200
    And The user list has at least 1 user whose name starts with C

  Scenario: TEST 3
    When I request user data
    Then Response is 200
    And The user list has at least 1 user and i display it

 Scenario: TEST 4
    When I navigate to site https://www.saucedemo.com/
    And I log in as standard_user with password secret_sauce
    And I click on "Add to cart" button in the backpack item and see the item added
    And I click on the shopping cart icon and click on the "Checkout" button
    And I set NameExample, LastnameExample, ZipExample for First Name, Last Name and Zip and click on Continue and then Finish
    Then I see my order dispached