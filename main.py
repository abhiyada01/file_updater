# Importing the basic libraries for this project
import glob
import os
import sqlite3
import sys
import time

from pandas import read_csv

'''
This program is design for MBO ATE
Author: Abhishek Kumar
Website: github.com
'''


class MyApp(object):
    def find_ad(self):
        # Get the address of file from text file
        with open('address_file.txt') as f:
            file_path = f.read()
            return file_path  # Return the file path in string format.

        #  Get the Latest modified file of specific directory of file.

    def file_mod_file(self):
        # Find the latest modified file in the Directory
        latest = max(glob.glob(self.find_ad()), key=os.path.getmtime)
        return latest  # return latest modified file

        #  Reading and modifying the csv data

    def get_csv_data(self):
        # CSV file & Data modification
        with open(self.file_mod_file()) as f_csv:
            data = read_csv(f_csv, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]).tail(2)
            # Find the null value present in the row and if present the remove it

            if data.iloc[1].isnull().any():
                com_data = data.iloc[1].combine_first(data.iloc[0])
                # print("With null value")
                return com_data
            else:
                # With out null value data
                com_data = data.iloc[1]
                # print("No Null value")
                return com_data

    def data_entry(self):
        # Get the PO number from barcode
        main_data = self.get_csv_data().to_dict()

        po = ('po', main_data["Barcode"][-11:-4])  # PO number from barcode
        po = ''.join(po)
        print(po)
        p_n = main_data["Barcode"].split('#')  # Get Part Number from barcode
        part_number = p_n[0]

        barcode = main_data["Barcode"]  # Get Barcode of card

        time_date = main_data["Date and Time"]  # Get the time and date

        op_name = main_data["Operator Name"]  # Get the operation name

        five_iso, five_iso_status = self.data_scraping(main_data, "5V ISO", 7.5, 9.0)  # Get Iso 5volt

        hvdc, hvdc_status = self.data_scraping(main_data, "HVDC", 140.0, 160.0)

        lv_12v, lv_12v_status = self.data_scraping(main_data, "12V LV", 15.0, 20.0)

        hv_12v, hv_12v_status = self.data_scraping(main_data, "12V HV", 11.60, 12.85)

        hv_5v, hv_5v_status = self.data_scraping(main_data, "5V HV", 7.5, 9.0)

        j2_volt, j2_volt_status = self.data_scraping(main_data, "J2(7 &10) Volt", -4.0, 2.50)

        q1_freq, q1_freq_status = self.freq_scraping(main_data, "Q1 Freq@ Volt", 44.00, 51.00, 5.00, 16.50)

        q15_freq, q15_freq_status = self.freq_scraping(main_data, "Q1 Freq@ Volt", 44.00, 51.00, 5.00, 16.0)

        q16_freq, q16_freq_status = self.freq_scraping(main_data, "Q1 Freq@ Volt", 44.00, 51.00, 5.00, 16.0)

        q2_freq, q2_freq_status = self.freq_scraping(main_data, "Q1 Freq@ Volt", 44.00, 51.00, 5.00, 16.0)

        q3_freq, q3_freq_status = self.freq_scraping(main_data, "Q1 Freq@ Volt", 44.00, 51.00, 5.00, 16.0)

        vdc_48, vdc_48_status = self.data_scraping(main_data, "48VDC", 46.0, 49.0)

        # Return the card testing status in string format
        card_status = str(five_iso_status & hvdc_status & hv_12v_status & lv_12v_status & hv_5v_status & hvdc_status &
                          j2_volt_status & q1_freq_status & q15_freq_status & q16_freq_status & q2_freq_status &
                          q3_freq_status & vdc_48_status)

        # print("PO Number =", po, '\n', "PCB Part Number =", part_number,
        # '\n', barcode, '\n', time_date, '\n', op_name,
        #       '\n', "Status of Card = ", card_status, '\n',
        #       "5 Volt ISO = ", five_iso, five_iso_status, '\n',
        #       "12 Volt HV = ", hv_12v, hv_12v_status, '\n',
        #       "12 Volt LV = ", lv_12v, lv_12v_status, '\n',
        #       "5 Volt HV = ", hv_5v, hv_5v_status, '\n',
        #       "HVDC = ", hvdc, hvdc_status, '\n',
        #
        #       "j2 = ", j2_volt, j2_volt_status, '\n',
        #       "Q1 Freq = ", q1_freq, q1_freq_status, '\n',
        #       "Q15 Freq = ", q15_freq, q15_freq_status, '\n',
        #       "Q16 Freq = ", q16_freq, q16_freq_status, '\n',
        #       "Q2 Freq = ", q2_freq, q2_freq_status, '\n',
        #       "Q3 Freq = ", q3_freq, q3_freq_status, '\n',
        #       "VDC = ", vdc_48, vdc_48_status
        #       )

        var = (barcode, time_date, card_status, op_name, five_iso, lv_12v, hv_12v, hv_5v, hvdc, j2_volt, q1_freq,
               q15_freq, q16_freq, q2_freq, q3_freq, vdc_48)

        try:
            conn = sqlite3.connect(part_number + ".db")
            cur = conn.cursor()

            create = "CREATE TABLE IF NOT EXISTS " + po + "(Barcode VARCHAR(255) PRIMARY KEY NOT NULL  ," \
                                                          "'Date_and_Time' VARCHAR(255), Status VARCHAR(10) NOT NULL," \
                                                          "'Operator Name' VARCHAR(75), '5V ISO' FLOAT(20), " \
                                                          "'HVDC' FLOAT(20),'12V LV' FLOAT(20),'12V HV' FLOAT(20)," \
                                                          "'5V HV' FLOAT(20), 'J2(7 &10) Volt' FLOAT(20)," \
                                                          "'Q1 Freq@ Volt' VARCHAR(75), 'Q15 Freq@ Volt' VARCHAR(75)," \
                                                          "'Q16 Freq@ Volt' VARCHAR(75), 'Q2 Freq@ Volt' VARCHAR(75)," \
                                                          " 'Q3 Freq@ Volt)' VARCHAR(75), '48VD' FLOAT(20)) "

            cur.execute(create)
            cur.execute("INSERT INTO " + po + " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", var)
            conn.commit()
            conn.close()
            print(barcode)
            # print("Command executed")
        except Exception as e:
            # print(e)
            pass

    def data_scraping(self, input_data, key_value, lower_limit, upper_limit):
        val = (input_data[key_value])
        if lower_limit < val < upper_limit:
            val_status = True
            return val, val_status
        else:
            val_status_f = False
            return val, val_status_f

    def freq_scraping(self, input_data, key_value, freq_lower, freq_upper, lower_limit, upper_limit):
        val_a = (input_data[key_value])
        val = (input_data[key_value]).split()
        freq = float(val[0][:-3])
        voltage = float(val[1].split('@')[1][:-1])

        if lower_limit < voltage < upper_limit and freq_lower < freq < freq_upper:
            val_status = True
            return val_a, val_status
        else:
            val_status_f = False
            return val_a, val_status_f

    # Loop mode
    def run_in_loop(self):
        file = self.file_mod_file()
        file_count = 0.0

        while True:
            file_time = os.path.getmtime(file)
            if file_time > file_count:
                print("New modified :", file_time)
                self.data_entry()
                file_count = file_time
            else:
                print("No Modification")
            time.sleep(4)


# Application function definition
def Application():
    try:
        MyApp().run_in_loop()
    except Exception as e:
        sys.exit(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Application()
