import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.") 
    a = np.array(list).reshape(3,3)

    mean = [np.mean(a, axis=0).tolist(),np.mean(a, axis=1).tolist(),np.mean(a).tolist()]
    variance = [np.var(a, axis=0).tolist(),np.var(a, axis=1).tolist(),np.var(a).tolist()]
    standard_deviation = [np.std(a,axis=0).tolist(),np.std(a,axis=1).tolist(),np.std(a).tolist()]
    maxa = [np.max(a,axis=0).tolist(),np.max(a,axis=1).tolist(),np.max(a).tolist()]
    mina = [np.min(a,axis=0).tolist(),np.min(a,axis=1).tolist(),np.min(a).tolist()]
    suma = [np.sum(a,axis=0).tolist(),np.sum(a,axis=1).tolist(),np.sum(a).tolist()]

    return {"mean": mean, "variance": variance, "standard_deviation": standard_deviation, "max":maxa, "min": mina, "sum":suma}

if __name__ == "__main__":
    print(calculate([0,1,2,3,4,5,6,7,8]))