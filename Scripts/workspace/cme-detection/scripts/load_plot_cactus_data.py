def parse_cactus_file(filepath):
    """
    Parses a Cactus file and returns a list of CME times.
    
    Parameters:
    filepath (str): The path to the Cactus file to be parsed.
    
    Returns:
    list: A list of CME times extracted from the file.
    """
    cme_times = []
    with open(filepath, 'r') as file:
        for line in file:
            # Assuming the CME times are in a specific format in the file
            # This is a placeholder for actual parsing logic
            if line.strip():  # Check if the line is not empty
                cme_times.append(line.strip())
    return cme_times


def plot_cme(cme_times):
    """
    Plots the CME times on a timeline.
    
    Parameters:
    cme_times (list): A list of CME times to be plotted.
    """
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from datetime import datetime

    # Convert string times to datetime objects
    dates = [datetime.strptime(time, '%Y-%m-%d %H:%M:%S') for time in cme_times]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, [1]*len(dates), 'ro')  # Plotting as red dots
    plt.yticks([])  # Hide y-axis ticks
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.gcf().autofmt_xdate()  # Rotate date labels
    plt.title('CME Occurrences Timeline')
    plt.xlabel('Date')
    plt.grid()
    plt.show()