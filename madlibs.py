stories = ["1. Hall Pass 1", "2. Hall Pass 2", "3. Hall Pass 3"]
print("\n".join(stories))
story_choice = input("Which story do you want? Enter 1, 2, or 3: ")
def storybegin(story):
    if story.strip() == "1":
        word1 = input("Name: ")
        word2 = input("Adjective: ")
        word3 = input("Noun: ")
        print("Please excuse %s, who is far too %s to attend %s class." 
        % (word1.strip().lower().capitalize(), word2.strip(), word3.strip()))
        again = input("Want to hear another story? (y or n): ")
        if again.lower().strip() == "y":
            story_choice = input("Which story do you want? Enter 1, 2, or 3: ")
            storybegin(story_choice) 
    elif story.strip() == "2":
        word1 = input("Name: ")
        word2 = input("Part of the body: ")
        word3 = input("Type of fluid: ")
        word4 = input("A substance: ")
        print("%s is sick with the %s flu. Drink more %s and take %s as needed." 
        % (word1.strip().lower().capitalize(), word2.strip(), word3.strip(), word4.strip()))
        again = input("Want to hear another story? (y or n): ")
        if again.lower().strip() == "y":
            story_choice = input("Which story do you want? Enter 1, 2, or 3: ")
            storybegin(story_choice) 
    elif story.strip() == "3":
        word1 = input("Name: ")
        word2 = input("A place: ")
        word3 = input("Noun: ")
        print("%s is authorized to be at %s instead of %s class." 
        % (word1.strip().lower().capitalize(), word2.strip(), word3.strip()))
        again = input("Want to hear another story? (y or n): ")
        if again.lower().strip() == "y":
            story_choice = input("Which story do you want? Enter 1, 2, or 3: ")
            storybegin(story_choice)
    else: 
        story_choice = input("Invalid choice; pick again (1, 2, or 3?): ") 
        storybegin(story_choice)

storybegin(story_choice)



