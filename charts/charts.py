import matplotlib.pyplot as plt

def generate_chart():
    labels = ['A', 'B', 'C', 'D']
    values = [1, 2, 3, 4]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)  # Los valores deben ir primero

    plt.savefig('pie.png')
    plt.close()