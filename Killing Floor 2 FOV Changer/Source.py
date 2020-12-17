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
pass;

def read_file(path):
    with open(kfengine_path, 'r') as file:
        data = file.readlines();
        return data;
    pass;       
pass;

def write_file(path, data):
    with open(path, 'w') as file:
        file.writelines(data);
    pass;
pass;

if (path.exists(kfengine_path)):
    data = read_file(kfengine_path);
    fovIndex = find_index("AspectRatioAxisConstraint", data);

    print('Enter 1 for Wide FOV\nEnter 2 for Narrow FOV');
    fovType = int(input());

    if (fovType == 1):
        data[fovIndex] = wide_fov;
    elif(fovType == 2):
        data[fovIndex] = narrow_fov;

    print("Writing Changes To KFEngine.ini File...");

    write_file(kfengine_path, data);

    print("Done. You Can Close The Program Now");
    pass;