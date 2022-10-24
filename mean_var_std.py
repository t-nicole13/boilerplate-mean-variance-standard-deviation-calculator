import numpy as np

def calculate(list):
        try:
                x = np.array(list).reshape(3,3)
                x_f = x.flatten()
                calculations = {
                    'mean': [np.mean(x, axis=0), np.mean(x, axis=1), np.mean(x_f)],
                    'variance':[np.var(x, axis=0), np.var(x, axis=1), np.var(x_f)],
                    'standard deviation':[np.std(x, axis=0), np.std(x, axis=1), np.std(x_f)],
                    'max':[np.max(x, axis=0), np.max(x, axis=1), np.max(x_f)],
                    'min':[np.min(x, axis=0), np.min(x, axis=1), np.min(x_f)],
                    'sum':[np.sum(x, axis=0), np.sum(x, axis=1), np.sum(x_f)]
                }

                return calculations

        except ValueError:
            print('List must contain nine numbers')




    