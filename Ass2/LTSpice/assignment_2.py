from apply_ltspice_filter import apply_ltspice_filter
import matplotlib.pyplot as pl
import numpy as np
import csv
import sys

class assignment_2:
    
    def __init__(self, input_file_name, circuit_name):
        self.input_file_name = input_file_name
        self.circuit_name = circuit_name

        
    def apply_configuration(self, time, signal_a, circuit_name):
        configuration = {
        }
        dummy, signal_b, signal_c = apply_ltspice_filter(
                circuit_name,
                time, signal_a,
                params=configuration
                )
        return list(signal_b), list(signal_c)

    def read_input_file(self, file_string):
        with open(file_string, "r", newline="") as f:
            reader = csv.reader(f)
            csv_file = {}
            csv_file['time'] = []
            csv_file['amplitude'] = []
            for row in reader:
                csv_file['time'].append(float(row[0]))
                csv_file['amplitude'].append(float(row[1]))
        return csv_file

    def save_output_file(self, file_string, dict_data):
        zd = zip(*dict_data.values())
        with open(file_string, 'w') as file:
            writer = csv.writer(file, delimiter=',', lineterminator = '\n')
            writer.writerow(dict_data.keys())
            writer.writerows(zd)

    def plot_output(self, time, input_pulses, beat_pulses, rate_analogue):

        fig, ax1 = pl.subplots(figsize = (14,5))
        ax1.plot(time, input_pulses, label ='Vin', color = 'red', alpha = 0.75)
        ax1.set_xlabel('Time (s)', fontsize = 15)
        ax1.set_ylabel('Vin (V)', fontsize = 15)

        ax2 = ax1.twinx()
        ax2.plot([time[0]], [input_pulses[0]], label = 'Vin', color = 'red')
        ax2.plot(time, beat_pulses, label ='V(beat_pulses)')
        ax2.plot(time, rate_analogue, label ='V(rate_analogue)')


        ax2.set_ylabel('Vout (V)', fontsize = 15)
        ax2.legend(loc = 1)
        pl.savefig("figure.png", bbox_inches='tight')
        pl.close()
        
    def run(self):
        
        input_data = self.read_input_file(self.input_file_name)
        output_data = {}
        output_data['time'] = input_data['time']
        output_data['beat_pulses'], output_data['rate_analogue'] = self.apply_configuration(input_data["time"], input_data["amplitude"], self.circuit_name)
        if(len(output_data['rate_analogue']) < 1):output_data['rate_analogue'] = [0]*len(output_data['time']) # Safety check encase V(RateAnalogue) isn't used
        self.plot_output(output_data['time'], input_data['amplitude'], output_data['beat_pulses'], output_data['rate_analogue'])
        self.save_output_file("Output.csv", output_data)


if __name__ == '__main__':
    
    file = sys.argv[1]
    circuit = sys.argv[2]
    run = assignment_2(file, circuit)
    run.run()