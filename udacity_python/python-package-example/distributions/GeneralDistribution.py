class Distribution:
    def __init__(self, mu=0, sigma = 1):
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def read_data_file(self, file_name, sample= True):
        """Function to read in data from a txt file. The txt file should have one number(float) per line. 
        After reading in the file, the mean and standard deviation are calculated

        Args:
            file_name(string): name of a fike to read from

        Returns:
             None
        """
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
            file.close()

            self.data = data_list 
            self.mean = self.calculate_mean()
            self.stdev = self.calculate_stvdev(sample)
