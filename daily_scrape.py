import ephem.retrieve.kutx989 as kutx989

# Put the main logic of the task in the main function.
def main(params):
    kutx989.main()
    print("parameters:", params)

    # You can return data to show outputs to users.
    # Outputs documentation: https://docs.airplane.dev/tasks/outputs
    return [
        {"element": "hydrogen", "weight": 1.008},
        {"element": "helium", "weight": 4.0026}
    ]
