def Strongest_Extension(class_name, extensions):
    max_strength = -float('inf')
    strongest_extension_name = ""

    for extension in extensions:
        cap_count = 0
        sm_count = 0
        for char in extension:
            if char.isupper():
                cap_count += 1
            elif char.islower():
                sm_count += 1
        
        current_strength = cap_count - sm_count
        
        if current_strength > max_strength:
            max_strength = current_strength
            strongest_extension_name = extension
            
    return f"{class_name}.{strongest_extension_name}"