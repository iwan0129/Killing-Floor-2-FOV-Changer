from os import path;

documents_folder = path.expanduser('~\Documents') + "\My Games\KillingFloor2\KFGame\Config"
kfengine_path = documents_folder + "\KFEngine.ini";
wide_fov = 'AspectRatioAxisConstraint=AspectRatio_MaintainYFOV\n'
narrow_fov = 'AspectRatioAxisConstraint=AspectRatio_MaintainXFOV\n'

def find_index(searchPattern, data):
    result = [value for value in data if searchPattern in value];

    if (result):
        return data.index(result[0]);
    else:
        return 0;

def read_file(path):
    file = open(kfengine_path, 'r');
    data = file.readlines();
    file.close();
    return data;

def write_file(path, data):
    file = open(path, 'w');
    file.writelines(data);
    file.close();

if (path.exists(kfengine_path)):
    data = read_file(kfengine_path);
    fovIndex = find_index("AspectRatioAxisConstraint", data);

    print('Enter 1 for Wide FOV\nEnter 2 for Narrow FOV');
    fovType = int(input());

    if (fovType == 1):
        data[fovIndex] = wide_fov;
    elif(fovType == 2):
        data[fovIndex] = narrow_fov;

    write_file(kfengine_path, data);