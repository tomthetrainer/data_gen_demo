# EventStore Retail POS Tutorial

## Step 1: Install the python extension 

Run this in the terminal

`code --install-extension ms-python.python`

## Step 2: Start KurrentDB

Run `./start_db.sh` in a terminal window

## Step 3: Start the data generator

Run `./start_data_server.sh` in the terminal window

This process will run in the foreground of your terminal, so you will have to use the teeny little plus sign on the top right of the terminal to launch another one if needed. 

## Step 4: Run the Example code

Open `example_reader.py`

And click the run button. 

If you didn't install the plugin, open a terminal and run 
`python example_reader.py`

## Step 5: View the stream browser 

You should see a stream `choose_a_stream_name` with an event `your_event_name`, the event will contain JSON that looks like this.

```

{
  "Date": "13/03/2025 02:45:06",
  "Store ID": "S003",
  "Product ID": "P0002",
  "Category": "Groceries",
  "Region": "South",
  "Inventory Level": "405",
  "Units Sold": "296",
  "Units Ordered": "30",
  "Demand Forecast": "304.13",
  "Price": "30.47",
  "Discount": "5",
  "Weather Condition": "Rainy",
  "Holiday/Promotion": "0",
  "Competitor Pricing": "31.38",
  "Seasonality": "Autumn"
}


```

## Step 6: FIX THIS MESS

First, reset KurrentDB to get rid of those poorly named streams and events. 

run `./start_db.sh` and you will have an empty database. 

### Things to ponder? 

What should you name your streams? 

One stream per store? 

One per Product ID?

How will you leverage projections? 

Etc.., I could go on, 

## Hope you like the demo
