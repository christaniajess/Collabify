# Collabify

<p align="center">
  <img src="Frontend\Readme_files\logo.jpg" width=600px>
</p>


# Project

1. [Project Report & API Docs](https://docs.google.com/document/d/1qe-v97qh0Op3Mk3ixpWzRCELSHMURxqcJao1n8w-aEI/edit)
2. [Project Slides](https://smu-my.sharepoint.com/:p:/g/personal/muhammadlim_2022_scis_smu_edu_sg/ERqi2dWXyB9GvByIzQPJ-TcBi2VPLSwgefTgUpb4jqM9GA?e=eU6zYl)
3. [Project Video]()

# Contributors

**G2 Team 1**

<table>
    <tr>
        <td align="center"><img src="Frontend\Readme_files\jesslyn.JPG" width="150px"/><br /><sub><b>Jesslyn Hilda Christania</b></sub></a></td>
        <td align="center"><img src="Frontend\Readme_files\justin.jpg" width="150px"/><br /><sub><b>Justin Arnold Sasam Rezaba</b></sub></a></td>
        <td align="center"><img src="Frontend\Readme_files\micole.jpg" width="150px"/><br /><sub><b>Micole John Evangelio Dela Cruz</b></sub></a></td>
        <td align="center"><img src="Frontend\Readme_files\izz.jpg" width="210px" height="195px"/><br /><sub><b>Izz Danial Bin Sharudin</b></sub></a></td>
        <td align="center"><img src="Frontend\Readme_files\danish.jpg" width="150px"/><br /><sub><b>Muhammad Danish Lim Bin Azri Aldrin Lim Teck Guan</b></sub></a></td>
        <td align="center"><img src="Frontend\Readme_files\jinming.jpg" width="150px"/><br /><sub><b>Cao Jinming</b></sub></a></td>
    </tr>
</table>

## Getting Started

### Dependencies

1. Vue.js
2. Docker
3. ZeroTier VPN

## Setup

### Setting up Backend

#### Downloading the Databases

1. Open up Collabify file and phpMyAdmin on browser
2. Go to `Backend` folder
3. Download the sql file `Setup.sql` from both `esd_external` and `esd_internal` folders
4. Import the files into PhpMyAdmin database

#### Testing connection to the various databases through Postman

1. Go onto Postman
2. import API `https://api.postman.com/collections/29873460-4253da8d-143d-4116-bae3-50edeb52a3c5?access_key=PMAT-01HTGXFM10TJHVDJTP0Q80DH08`
3. Go to Environments tab then Globals
4. Set variable `baseUrl` intial value and current value to the ip address hosting the databases 

#### Running the External and Internal yaml file

1. Edit the internal and external compose.yaml file and change the ip addresses to the ip address according to the machine hosting esd_internal and esd_external. For compose.yaml under esd_internal, change the IP to the machine hosting esd_external, vice versa
2. Open `esd_external` folder in the terminal
3. Run `docker compose up`
4. Open `esd_internal` folder in the terminal
5. Run `docker compose up`

### Setting up Frontend

1. Open terminal in vscode for Project folder
2. Edit the project > src > service > constant.js file ip address under Microservice to the machine running esd_external
3. Run `npm install`
4. Run `npm run dev` to run the vue
5. copy paste the url from the terminal to the browser

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.

- [PrimeVue](https://github.com/primefaces/sakai-vue)
- [Stipe Payment](https://github.com/WebDevSimplified/stripe-checkout-simple)
