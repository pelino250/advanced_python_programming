# Pagination is a technique of dividing a large set of data
# into smaller manageable chunks or pages.

# pagination techniques:
# 1. Offset-based pagination
# 2. Cursor-based pagination
# 3. Keyset-based pagination

def paginate_data(data, page_number, page_size):
    # Calculate start and end indices
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size

    # Return a slice of the data
    return data[start_index:end_index]


# Sample data
data = list(range(1, 101))  # A list of numbers from 1 to 100

# Get the first page of data (first 10 items)
page_1 = paginate_data(data, page_number=1, page_size=10) # 0-9
print(page_1)

# Get the second page of data (next 10 items)
page_2 = paginate_data(data, page_number=2, page_size=10)
print(page_2)
