import matplotlib.pyplot as plt
import numpy as np


def draw_linear_nn(weights, biases, input_labels=None, output_labels=None, cmap='seismic'):
    """
    Draws a simple 4-input -> 4-output linear network.
    weights: numpy array shape (4,4), biases: numpy array shape (4,)
    """
    n_inputs, n_outputs = weights.shape
    # positions for nodes
    x_input, x_output = 0.1, 0.9
    y_input = np.linspace(0.9, 0.1, n_inputs)
    y_output = np.linspace(0.9, 0.1, n_outputs)

    fig, ax = plt.subplots(figsize=(6, 6))
    # draw nodes
    ax.scatter([x_input]*n_inputs, y_input, s=500, c='lightblue', zorder=3)
    ax.scatter([x_output]*n_outputs, y_output, s=500, c='lightgreen', zorder=3)

    # draw input labels
    if input_labels is None:
        input_labels = [f'in{i}' for i in range(n_inputs)]
    for i, label in enumerate(input_labels):
        ax.text(x_input - 0.05, y_input[i], label, ha='right', va='center')
    # draw output labels
    if output_labels is None:
        output_labels = [f'out{j}' for j in range(n_outputs)]
    for j, label in enumerate(output_labels):
        ax.text(x_output + 0.05, y_output[j], label, ha='left', va='center')

    # draw connections with width and color based on weight
    max_w = np.max(np.abs(weights)) if np.any(weights) else 1
    for i in range(n_inputs):
        for j in range(n_outputs):
            w = weights[i, j]
            norm = w / max_w
            color = 'red' if w > 0 else 'blue'
            ax.add_line(plt.Line2D([x_input, x_output], [y_input[i], y_output[j]],
                                     linewidth=2 + 4 * abs(norm), color=color, alpha=0.6))

    # annotate biases
    for j in range(n_outputs):
        b = biases[j]
        ax.text(x_output, y_output[j] - 0.05, f'bias={b:.2f}', ha='center', va='top')

    ax.axis('off')
    plt.title('4x4 Linear NN Visualization')
    plt.show()


if __name__ == '__main__':
    # Example: random network or load from boom_evolve-empty
    try:
        import boom_evolve_empty
    except ImportError:
        pass
    # Random example network
    W = np.random.randn(4, 4)
    B = np.random.randn(4)
    draw_linear_nn(W, B)
