import mlflow


def calculate(X,y):
    return (X-y)



if __name__ == '__main__':
    X,y=100905,2002245
    with mlflow.start_run():
        result=calculate(X,y)
        print(f" my result is {result}")
        mlflow.log_param("X", X)
        mlflow.log_param("y", y)
        mlflow.log_param("result",result)
        
        