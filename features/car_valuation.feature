Feature: Car Valuation

  Scenario Outline: Validate car details using registration number
    Given I navigate to the car valuation website
    When I search for a car with registration with "<registration>"
    And I enter the car "<mileage>"
    Then the car details should match the expected output
    Examples:
      | registration | mileage |
      | AD58 VNF     | 33000   |
#      | BW57 BOW     |24000|

