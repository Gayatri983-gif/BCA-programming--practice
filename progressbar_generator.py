def generate_github_progress_bar(topic, percentage, total_blocks=15):
    """
    Generates a visual progress bar for a GitHub README.
    """
    if percentage > 100:
        percentage = 100
    elif percentage < 0:
        percentage = 0
        
    # Calculate how many filled vs empty blocks to show
    filled_blocks = int((percentage / 100) * total_blocks)
    empty_blocks = total_blocks - filled_blocks
    
    # Create the visual bar using solid and light Unicode blocks
    bar = "█" * filled_blocks + "░" * empty_blocks
    
    # Format the final Markdown output
    markdown_output = f"### 🚀 {topic}\n"
    markdown_output += f"`[{bar}] {percentage}%`\n"
    
    return markdown_output

if __name__ == "__main__":
    print("--- GitHub Profile Progress Bar Generator ---\n")
    
    # Example inputs (You can change these values to test)
    my_topic = "Python Basic to Advanced Goal"
    my_percentage = 15 
    
    result = generate_github_progress_bar(my_topic, my_percentage)
    
    print("Copy the text below and paste it into your README.md:\n")
    print(result)
