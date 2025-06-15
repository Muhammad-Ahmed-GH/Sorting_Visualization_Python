from algorithms import *
from visuals import *
from shared import *


def generate_data():
    try:
        size = int(size_entry.get())
        if size < 1:
            raise ValueError

        data.clear()
        data.extend([random.randint(10, 300) for _ in range(size)])
        draw_bars(data, ['#00B294'] * len(data))
    except:
        messagebox.showwarning("Invalid Input", "Please enter a valid size.")

def start_sorting():
    selected_algo = algo_combobox.get()
    time
    if selected_algo == "Bubble Sort":
        bubble_sort()
    elif selected_algo == "Insertion Sort":
        insertion_sort()
    elif selected_algo == "Selection Sort":
        selection_sort()
    elif selected_algo == "Merge Sort":
        merge_sort()
    else:
        messagebox.showwarning("Warning", "Please choose a sorting algorithm")


generate_button = tk.Button(frame, text="Generate Data", command=generate_data)
generate_button.grid(row=0, column=0, padx=5)

algo_combobox = ttk.Combobox(frame, values=["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort"])
algo_combobox.set("Bubble Sort")
algo_combobox.grid(row=0, column=1, padx=5)

sort_button = tk.Button(frame, text="Start Sorting", command=start_sorting)
sort_button.grid(row=0, column=2, padx=5)


size_label = tk.Label(frame, text="Input Size:")
size_label.grid(row=0, column=4, padx=5)
size_entry = tk.Entry(frame, width=5)
size_entry.insert(0, "20")
size_entry.grid(row=0, column=5, padx=5)

generate_data()

''' comparison
algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Merge Sort": merge_sort
}
results = {}
num_trials = 10

data_copy = data.copy()

for algo_name, algo_func in algorithms.items():
    total_time = 0
    for _ in range(num_trials):
        
        data[:] = data_copy

        start_time = time.perf_counter()
        algo_func()
        end_time = time.perf_counter()

        total_time += (end_time - start_time)

    avg_time = total_time / num_trials
    results[algo_name] = avg_time

print(results)
'''

root.mainloop()