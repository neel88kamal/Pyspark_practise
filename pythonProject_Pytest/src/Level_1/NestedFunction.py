def message_one():
    global message_two
    def message_two():
        global message_three
        def message_three():
            print("hello from three")
        message_three()
        print("hello from two")
    message_two()
    message_three()
    print("hello from one")

message_one()
message_two()
message_three()
