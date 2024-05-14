import sys

def fcfs(initialPosition, requests):
    headMovement = 0
    currentPosition = initialPosition
    
    for request in requests:
        headMovement += abs(request - currentPosition)
        currentPosition = request
    
    return headMovement

def scan(initialPosition, requests, maxCylinder):
    headMovement = 0
    currentPosition = initialPosition
    requests.sort()
    
    lessThanInitial = [r for r in requests if r < initialPosition]
    greaterThanInitial = [r for r in requests if r >= initialPosition]
    
    for request in greaterThanInitial:
        headMovement += abs(currentPosition - request)
        currentPosition = request

    if lessThanInitial:
        headMovement += abs(currentPosition - maxCylinder)
        currentPosition = maxCylinder


        headMovement += maxCylinder 
        currentPosition = 0

        for request in lessThanInitial:
            headMovement += abs(currentPosition - request)
            currentPosition = request
    
    return headMovement

def c_scan(initialPosition, requests, maxCylinder):
    headMovement = 0
    currentPosition = initialPosition
    requests.sort()
    
    lessThanInitial = [r for r in requests if r < initialPosition]
    greaterThanInitial = [r for r in requests if r >= initialPosition]
    
    for request in greaterThanInitial:
        headMovement += abs(currentPosition - request)
        currentPosition = request

    if lessThanInitial:
        headMovement += abs(currentPosition - maxCylinder)
        currentPosition = 0
        headMovement += maxCylinder  

        for request in lessThanInitial:
            headMovement += abs(currentPosition - request)
            currentPosition = request
    
    return headMovement

def readRequestsFromFile(file_name):
    with open(file_name, 'r') as file:
        requests = [int(line.strip()) for line in file]
    return requests

def main():
    if len(sys.argv) != 3:
        print("Usage: python disk_scheduling.py initialPosition requests_file")
        return
    
    initialPosition = int(sys.argv[1])
    requests_file = sys.argv[2]
    
    maxCylinder = 4999
    
    requests = readRequestsFromFile(requests_file)
    
    print("FCFS Head Movements:", fcfs(initialPosition, requests.copy()))
    print("SCAN Head Movements:", scan(initialPosition, requests.copy(), maxCylinder))
    print("C-SCAN Head Movements:", c_scan(initialPosition, requests.copy(), maxCylinder))

if __name__ == "__main__":
    main()
