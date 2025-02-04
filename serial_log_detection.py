import serial
import time

def main():
    port = '/dev/cu.usbmodem1101'  # <-- Change to your actual serial port
    baud = 115200                 # Must match the Arduino Serial.begin(115200)

    # Open the serial port
    with serial.Serial(port, baud, timeout=1) as ser, open('data.txt', 'w') as f:
        # Give the Arduino a moment to reset after opening the port
        time.sleep(2)

        print("Connected to Arduino on", port)
        print("Type an integer between 1 and 100 (representing number of data points you want to collect, or 'quit' "
              "to exit.")
        print()

        count = 0
        # print the 5 intiial lines of code. acutal collection data handled later if this doesn't work so no worries
        for _ in range(5):
            line = ser.readline().decode('utf-8', errors='replace')
            print(line, end='')
        while True:
            # Check if there's any line coming from Arduino
            if count > 0:
                # make sure the first line read is the BEGINNING marker, skip all other lines
                ready = True
                while ready:
                    line = ser.readline().decode('utf-8', errors='replace')
                    print(line)
                    if line == "BEGINNING\n":
                        ready = False
                for _ in range(count):
                    if ser.in_waiting > 0:
                        # note that this matches the arduino logging output. needs to be consistennt
                        line_acc = ser.readline().decode('utf-8', errors='replace')
                        line_vel = ser.readline().decode('utf-8', errors='replace')
                        line_temp = ser.readline().decode('utf-8', errors='replace')
                        line_empty = ser.readline().decode('utf-8', errors='replace')
                        # Print whatever Arduino sends
                        if line_acc:
                            print(line_acc, end='')
                            f.write(line_acc)
                        if line_vel:
                            f.write(line_vel)
                            print(line_vel, end='')
                        if line_temp:
                            f.write(line_temp)
                            print(line_temp, end='')
                        if line_empty:
                            f.write(line_empty)
                            print(line_empty, end='')
                        # print()
                    time.sleep(.5) # TODO need to set this to GLOBAL_DT value eventually
                print("Data collection complete.")
                f.flush()
                ser.write(('c' + '\n').encode('utf-8')) # tells arduino to stop collecting data
            count = 0
            # Optionally, let user type commands in Python console
            user_input = input("Enter integer or 'quit': ").strip()
            if user_input.lower() == 'quit':
                print("Exiting...")
                f.close()
                break
            elif int(user_input) > 0 and int(user_input) <= 100:
                # Send command to Arduino
                count = int(user_input)
                print(f"Collecting {user_input} data points:")
                ser.write(('z' + '\n').encode('utf-8')) # tells arduino to start collecting, then gives it a second
                time.sleep(1)
            else:
                print("Unknown command. Type an integer between 1 and 100, or 'quit'.")

if __name__ == "__main__":
    main()