/* link: 
https://leetcode.com/problems/combine-two-tables/description/ 
*/

SELECT (
    Person.lastName,
    Person.firstName,
    Address.city,
    Address.state
)
FROM Person
LEFT JOIN Address
ON Person.personId = Address.personId