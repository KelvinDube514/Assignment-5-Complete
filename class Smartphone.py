class Smartphone:
    def __init__(self, brand, model, os, screen_size, battery_capacity, price):
        self.brand = brand
        self.model = model
        self.os = os
        self.screen_size = screen_size  # in inches
        self.battery_capacity = battery_capacity  # in mAh
        self.price = price
        self.is_powered_on = False
        self._apps_installed = []  # encapsulated attribute
        
    def __str__(self):
        return f"{self.brand} {self.model} - OS: {self.os}, Screen: {self.screen_size}\", Battery: {self.battery_capacity}mAh, Price: ${self.price}"
    
    def power_toggle(self):
        """Toggles the power state of the smartphone."""
        self.is_powered_on = not self.is_powered_on
        status = "on" if self.is_powered_on else "off"
        return f"Phone is now powered {status}."
    
    def install_app(self, app_name):
        """Installs an app on the smartphone."""
        if not self.is_powered_on:
            return "Cannot install app. Phone is powered off."
        
        if app_name in self._apps_installed:
            return f"{app_name} is already installed."
        
        self._apps_installed.append(app_name)
        return f"{app_name} has been installed successfully."
    
    def get_installed_apps(self):
        """Returns a list of installed apps."""
        if not self.is_powered_on:
            return "Cannot retrieve apps. Phone is powered off."
        
        if not self._apps_installed:
            return "No apps installed."
        
        return self._apps_installed
    
    def calculate_discount_price(self, discount_percentage):
        """Calculates the discounted price of the smartphone."""
        if 0 <= discount_percentage <= 100:
            discount_amount = self.price * (discount_percentage / 100)
            return self.price - discount_amount
        else:
            return "Invalid discount percentage."


class FlagshipSmartphone(Smartphone):
    def __init__(self, brand, model, os, screen_size, battery_capacity, price, 
                 camera_specs, water_resistance_rating, special_features):
        super().__init__(brand, model, os, screen_size, battery_capacity, price)
        self.camera_specs = camera_specs  # e.g., "Triple 48MP+12MP+8MP"
        self.water_resistance_rating = water_resistance_rating  # e.g., "IP68"
        self.special_features = special_features  # list of special features
        self._performance_mode = "Normal"  # encapsulated attribute with default value
    
    def __str__(self):
        return f"{super().__str__()}, Camera: {self.camera_specs}, Water Resistance: {self.water_resistance_rating}"
    
    def set_performance_mode(self, mode):
        """Sets the performance mode of the flagship smartphone."""
        if not self.is_powered_on:
            return "Cannot change performance mode. Phone is powered off."
        
        valid_modes = ["Normal", "Power Saving", "Ultra Performance", "Gaming"]
        if mode not in valid_modes:
            return f"Invalid mode. Choose from: {', '.join(valid_modes)}"
        
        self._performance_mode = mode
        return f"Performance mode set to {mode}."
    
    def get_performance_mode(self):
        """Returns the current performance mode."""
        if not self.is_powered_on:
            return "Cannot retrieve performance mode. Phone is powered off."
        
        return f"Current performance mode: {self._performance_mode}"
    
    def calculate_discount_price(self, discount_percentage):
        """Overrides the parent method to apply a maximum discount for flagship phones."""
        if discount_percentage > 15:
            print("Note: Maximum discount for flagship models is 15%.")
            discount_percentage = 15
        
        return super().calculate_discount_price(discount_percentage)
    
    def list_special_features(self):
        """Lists all special features of the flagship smartphone."""
        if not self.special_features:
            return "No special features available."
        
        return f"Special features: {', '.join(self.special_features)}"


# Example usage:
if __name__ == "__main__":
    # Create a basic smartphone
    basic_phone = Smartphone("Samsung", "Galaxy A52", "Android 11", 6.5, 4500, 399.99)
    print(basic_phone)
    
    # Power on the phone
    print(basic_phone.power_toggle())
    
    # Install some apps
    print(basic_phone.install_app("WhatsApp"))
    print(basic_phone.install_app("Instagram"))
    print(basic_phone.install_app("Spotify"))
    
    # Get installed apps
    print("Installed apps:", basic_phone.get_installed_apps())
    
    # Calculate discount
    print(f"Discounted price (20% off): ${basic_phone.calculate_discount_price(20):.2f}")
    
    print("\n" + "="*50 + "\n")
    
    # Create a flagship smartphone
    flagship_phone = FlagshipSmartphone(
        "Apple", "iPhone 13 Pro", "iOS 15", 6.1, 3095, 999.99,
        "Triple 12MP+12MP+12MP with LiDAR", "IP68",
        ["ProMotion display", "A15 Bionic chip", "Ceramic Shield", "MagSafe"]
    )
    print(flagship_phone)
    
    # Power on the phone
    print(flagship_phone.power_toggle())
    
    # Install some apps
    print(flagship_phone.install_app("FaceTime"))
    print(flagship_phone.install_app("Safari"))
    
    # Set performance mode
    print(flagship_phone.set_performance_mode("Ultra Performance"))
    print(flagship_phone.get_performance_mode())
    
    # List special features
    print(flagship_phone.list_special_features())
    
    # Calculate discount (with maximum limit)
    print(f"Discounted price (25% off, limited to 15%): ${flagship_phone.calculate_discount_price(25):.2f}")