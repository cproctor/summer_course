from twitter_log import TwitterLog

spammer = TwitterLog(
    "HVU3ROf8ICM4Ye5fbYc0o7EN0",
    "lbqMC6c7vxyRz8k6GA4IZHuusN9NvvieIGNxvmVASlRBQ01f7e" ,
    "3241290962-Srzd64RZIARwbUq6SBLOS2b1A3zbYPWxAA0YrYk", 
    "wE6TD6vXoLpBQ03ovNvSiyrnjS6CnFYuZWD05A0EMjBNB"
)

for each_number in range(100):
    spammer.info("Do you like the number {}? I do!".format(each_number))
