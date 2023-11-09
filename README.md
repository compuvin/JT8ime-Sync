<a name="readme-top"></a>
# JT8ime-Sync
Adjusts time based on FT8 stations heard

<!-- GETTING STARTED -->
## Getting Started

This script monitors the text file that is created by MSHV of all stations that it hears and makes adjustments to the time based on that. The process should work for other programs as well but will require some tweaking.

I designed this script to run on my portable "hilltopper" setup where getting an accurate time is  not always possible.

### Prerequisites

1. Root (or sudo) access to change time
2. MSHV (hope to support WSJT-X and JTDX in the future)

### Installation

There is nothing to install. Simply download the script, make it executible, and run!

1. Download the script
   ```sh
   wget https://raw.githubusercontent.com/compuvin/JT8ime-Sync/main/JT8ime-Sync.py
   ```
2. Make executible
   ```sh
   chmod +x JT8ime-Sync.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Start WSHV
2. Run the script
   ```sh
   sudo ./JT8ime-Sync.py
   ```
3. Enter the current date and time
4. Let the script work its magic

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Updating

Updating is simple, just download the updated file and replace the old one:

1. Change directories to wherever your copy of the script resides

2. Remove or rename your current script
3. Download the script
   ```sh
   wget https://raw.githubusercontent.com/compuvin/JT8ime-Sync/main/JT8ime-Sync.py
   ```
4. Make executible
   ```sh
   chmod +x JT8ime-Sync.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Support WSJT-X
- [ ] Support JTDX
- [ ] Make process faster and/or more accurate

See the [open issues](https://github.com/compuvin/jt8ime-sync/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GPL-3.0 license. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[![CodeFactor](https://www.codefactor.io/repository/github/compuvin/jt8ime-sync/badge)](https://www.codefactor.io/repository/github/compuvin/jt8ime-sync)
