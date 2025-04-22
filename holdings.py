# Build an API endpoint that clients can reach and submit their holdings data as a JSON payload. 
# The endpoint should evaluate each incoming holding against defined rules
# If there are violations, then return a list of these violations

#Pseudo code:
# for each holding:
#    for each rule:
#        if the holding violates the rule:
#            add to violations list


# ✅ Rules:
#    isin must be a 12-character string
#    value must be a positive number
#    currency must be one of: ["USD", "GBP", "EUR", "JPY"]






