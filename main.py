from typing import List


class Garage:
    def __init__(self):
        self.__total_space = 20
        self.__current_state: List[str] = []
        for ii in range(self.__total_space):
            self.__current_state.append("_")
        self.__cars = 0
        self.__vans = 0
        self.__motorcycles = 0

    def add_vehicle(self, vehicle_type: str) -> int:
        consecutive_spaces = 0
        for ii, cc in enumerate(self.__current_state):
            if cc == '_':
                if vehicle_type == 'c':
                    self.__current_state[ii] = 'c'
                    self.__cars += 1
                    return 0
                elif vehicle_type == 'm':
                    self.__current_state[ii] = 'm'
                    self.__motorcycles += 1
                    return 0
                else:
                    consecutive_spaces += 1
                    if consecutive_spaces >= 3:
                        self.__current_state[ii - 2] = 'v'
                        self.__current_state[ii - 1] = 'v'
                        self.__current_state[ii] = 'v'
                        self.__vans += 1
                        return 0
            else:
                consecutive_spaces = 0

        return 1


    def remove_vehicle(self, vehicle_type: str) -> int:
        successfully_found = False
        for ii, cc in enumerate(self.__current_state):
            if cc == vehicle_type:
                if vehicle_type == 'v':
                    self.__current_state[ii] = '_'
                    self.__current_state[ii + 1] = '_'
                    self.__current_state[ii + 2] = '_'
                    successfully_found = True
                    break
                else:
                    self.__current_state[ii] = '_'
                    successfully_found = True
                    break

        match vehicle_type:
            case 'c':
                self.__cars -= 1
            case 'm':
                self.__motorcycles -= 1
            case 'v':
                self.__vans -= 1
            case _:
                print('Invalid vehicle type')

        return 0 if successfully_found else 1

    def get_state(self, is_raw: bool) -> tuple[int, int, int, List[str]]:
        if is_raw:
            return self.__cars, self.__motorcycles, self.__vans, self.__current_state
        else:
            summarized_state: List[str] = []
            ii = 0
            while ii < len(self.__current_state):
                match self.__current_state[ii]:
                    case 'c':
                        summarized_state.append('car')
                    case 'm':
                        summarized_state.append('motorcycle')
                    case 'v':
                        summarized_state.append('van')
                        ii += 2
                    case _:
                        summarized_state.append('empty')
                ii += 1
            return self.__cars, self.__motorcycles, self.__vans, summarized_state


if __name__ == '__main__':
    garage = Garage()
    print('Welcome to this absolutely glorious garage!')
    print('Enter vehicle type and leaving or entering: "car leaving" or "van entering", for example.')
    print('Enter "status" for the current state of the garage or "status raw" for the raw character list of the current garage state')
    print('Enter "exit" to lock it up and throw away the key\n')
    while True:
        action = input('> ').split()
        if 'status' in action:
            cars, motorcycles, vans, current_state = garage.get_state(True) if 'raw' in action else garage.get_state(False)
            cars_summary = f"There is {cars} car," if cars == 1 else f"There are {cars} cars,"
            motorcycles_summary = f"{motorcycles} motorcycle," if motorcycles == 1 else f"{motorcycles} motorcycles,"
            vans_summary = f"and {vans} van" if vans == 1 else f"and {vans} vans"

            print(f'\n{cars_summary} {motorcycles_summary} {vans_summary} parked in the garage')
            print(f"Here's what it looks like: {current_state}\n")
        elif 'exit' in action:
            print('\nLocked it up. See ya!')
            break
        elif action[1] == 'entering':
            match action[0]:
                case 'car':
                    result = "Successfully parked a car!" if garage.add_vehicle('c') == 0 else "No space left for a car in the garage :("
                case 'motorcycle':
                    result = "Successfully parked a motorcycle!" if garage.add_vehicle('m') == 0 else "No space left for a motorocycle in the garage :("
                case 'van':
                    result = "Successfully parked a van!" if garage.add_vehicle('v') == 0 else "No space left for a van in the garage :("
                case _:
                    print('\nInvalid vehicle type. Vehicle types are: car, van, motorcycle\n')
                    break

            print(f'\n{result}\n')
        elif action[1] == 'leaving':
            match action[0]:
                case 'car':
                    result = "Successfully removed a car!" if garage.remove_vehicle('c') == 0 else "Couldn't find any cars parked :("
                case 'motorcycle':
                    result = "Successfully removed a motorcycle!" if garage.remove_vehicle('m') == 0 else "Couldn't find any motorcycles parked :("
                case 'van':
                    result = "Successfully removed a van!" if garage.remove_vehicle('v') == 0 else "Couldn't find any vans parked :("
                case _:
                    print('\nInvalid vehicle type. Vehicle types are: car, van, motorcycle\n')
                    break

            print(f'\n{result}\n')
        else:
            print("\nImproper input\n")
