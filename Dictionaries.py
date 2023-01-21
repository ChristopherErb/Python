
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "April": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Dec"])

# invalid entry:
print(monthConversions.get("Pat", "Not a valid key"))