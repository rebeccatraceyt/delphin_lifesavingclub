<div style="margin:auto; text-align:center">
<img src="markdown-files/readme-files/readme-logo.png" alt="Delphin Logo" />
<h1> Image credits </h1>
</div>

[Return to README.md file](README.md "Link to README file")

[View live project](https://delphin-lifesavingclub.herokuapp.com/ "Link to Live project")

[View Repository](https://github.com/rebeccatraceyt/delphin_lifesavingclub "Link to Repository")

***

### Table of contents
1. [Testing User Stories](#Testing-User-Stories)
2. [Manual Testing](#Manual-Testing)
    1. [Common Elements Testing](#Common-Elements-Testing)
    2. [Page Elements Testing](#Page-Elements-Testing)
3. [Automated Testing](#Automated-Testing) 
     - [Code Validation](#Code-Validation)
     - [Browser Validation](#Browser-Validation)
     - [Lighthouse Auditing](#Lighthouse-Auditing)
4. [User Testing](#User-Testing)

***

<div style="text-align:center">
<img src="markdown-files/readme-files/delphin-res.png" alt="Delphin Responsivness Example" />
</div>

***

## Testing User Stories

User stories were tested to ensure the needs of the user were being met, with the following results:

### General Users

**1. As a user I want to view all products, to purchase my desired items.**
- In the `Shop` dropdown menu on the navigation menu, users have the selection to `Shop Apparel`, `Shop Courses` or `View All`.
- `View All` will direct users to the `All Products` page.
- There are breadcrumbs on both `All Apparel` and `All Courses` pages, allowing users quick access to the `All Product` page.

**2. As a user I want to filter through categories, to only see relevant products.**
- On all `Shop` pages, there are filters for categories, and sub-categories.
- The `All Products` page has the `Apparel` and `Courses` category button filters.
- The `Apparel` and `Courses` pages have their respective sub-category button filters (apparel type and age range).

**3. As a user I want to use a search query, to find a specific product or product type.**
- Users can use the category filters available on the `Shop` pages to quickly search for their product category.
- There is a `Search` page, distinguished by a conventional search icon on the navigation menu, directing users to the search page, where they can type in their query.

**4. As a user I want to add items to my shopping bag, to begin the order process.**
- On all product detail pages, there is a call-to-action button that allows users to add their desired product to their shopping bag.
- The user will not be able to view items in their shopping bag if they are not authenticated.

**5. As a user I want to receive visual feedback that my item has been added to the bag, to confirm my selection.**
- On clicking the `Add to Bag` button on the product detail page, a toast will provide feedback to the user that the product has been successfully added to their shopping bag.
- To view their shopping bag they will have to login.

**6. As a user I want to select a course on a specific day, to suit my needs.**
- Each course has their own specific class times and days.
- The user is able to select their preferred time/day using the `select` dropdown menu on the product details page.
- Each class provides information to the user of how many places are available for that particular class.

**7. As a user I want to select apparel in a specific size, to suit my needs.**
- Similar to the courses, all apparel products have a selection of sizes available.
- Users can select their size using the `select` dropdown menu.
- Each product provides information of the the stock numbers to the user.

**8. As a user I want to view contact information for the club, to communicate with team.**
- The `Contact` page is available in the `About` dropdown menu of the navigation menu. 
- Clicking it will direct users to the contact page, which provides multiple points of contact:
    - Phone Number link
    - Email address to notable Club Officers
    - A map pinpointing the clubs location
    - A Contact form for general enquiries

**9. As a user I want to connect with the club on one of their social apps, to communicate with the team.**
- On the footer (displayed on all pages, with the exception of the checkout pages) there are social links, providing quick access to the clubs social accounts:
    - Facebook
    - Whatsapp
    - Mailto

**10. As a user I want to get a breakdown of classes offered, to find one that suits my needs.**
- The `Academy Programme` page is located in the `About` dropdown list of the navigation menu.
- The page hosts an accordian feature with each class that the club offers housed in their own accordion, with the class name and age range as the title of each.
- Clicking their desired class will open the accordion, providing users with the necessary information about each.

**11. As a user I want to navigate to a page that could help me with my enquiry, to answer my question.**
- The `Frequently Asked Questions` page is located in the `About` dropdown list of the navigation menu.
- Similar to the Academy Programme page, the FAQs are displayed in a featured accordion, with each question as the title of the accordion card.
- Clicking the question opens the card, revealing the answer for the user.

**New Visitors**

**1. As a new visitor, I want to create an account, to unlock registered user features.**
- If the user is not authenticated, two links will be displayed on the navigation menu:
    - `Register`
    - `Login`
- Register will lead users to the signup page, allowing the user to enter their details and create their account.
- The register page is also availble on the login page for convenience.

**Returning Visitors**

**1. As a returning visitor, I want to easily log into my existing account, to unlock registered user features.**
- If the user is not authenticated, the login page will be clearly displayed on the navigation menu.
- Clicking it directs the user to the login page, where they can enter their details to log into their account.

**2. As a returning visitor, I want to view my previous orders, to keep a record of my transaction.**
- When a user is authenticated, a mew dropdown menu is displayed. The `Account` dropdown menu provides users with quick access to their order history.
- On the `Order History` page, the user will be presented with a table of their previous orders (if they have any) or conditional text.
- Each order displays the date of the order, the number of items and the grand total of the order.
- A call-to-action `View` button allows users to view the entire order details.

**3. As a returning visitor, I want to save default information, to save time for future orders.**
- On the `Account` dropdown menu, there is a quick link to the users profile page, there they can enter their default information for faster checkout.
- Additionally, the user can click the checkbox available on the checkout page to save their information.

**4. As a returning visitor, I want to edit default information, to update any necessary fields.**
- Directing to the user's profile page will display the user's saved default information.
- There they can edit their information, as needed, and click the call-to-action `Update` button.

**5. As a returning visitor, I want to view shopping bag to get an overview of products I wish to order.**
- When the user adds to their shopping bag, a toast will appear providing real-time information that the product was sucessfully added, as well as a snapshot of the contents currently in their bag.
- Clicking either the toast or the bag icon will direct the user to their shopping bag to view and edit as they wish.

**6. As a returning visitor, I want to remove products from my bag, to suit my needs.**
- In the shopping bag, there is a conventional `x` icon placed at the top-right of each product box.
- Clicking this item will remove the product from their shopping bag.

**7. As a returning visitor, I want to update a product's quantity, to suit my needs.**
- Within the shopping bag, the user can update the quantity of a particular product by using the prepending and appending buttons on the quantity box.
- They can then save their changes by clicking the call-to-action `Update` button.

**8. As a returning visitor, I want to get real-time feedback on available stock, to make purchase decisions.**
- Each product variation has it's own stock count displayed on the product details page.
- This provides users with real-time stock numbers, allowing them to select up that number.
- The buttons on the quantity box dynamically change, based on the stock count of the product selected and the quantity the user has inputted.

**8. As a returning visitor, I want to proceed to a secure checkout, to make a purchase.**
- In the shopping bag, a `Secure Checkout` button directs users to the first page of the checkout process.

**9. As a returning visitor, I want to have clear visual feedback of the order process, to understand all steps of the process.**
- Each step of the checkout process provides a Heads Up display of the checkout process. 
- This display changes page to page, with clear feedback to the user of their current location in the process.

**10. As a returning visitor, I want to be able to edit my bag at all times, to allow change of mind.**
- The user can edit their bag in the shopping bag.
- An Edit button is available on every page of the checkout process, allowing the users to return to their shopping bag for editing.

**11. As a returning visitor, I want to receive a summary of my order via email to confirm that my transaction has been process.**
- When a user successfully checks out, a confirmation email will be sent to their specified email address.
- This email will provide order information including the date, total and a list of ordered items.
- Further information, such as delivery times and course instructions are available in the email.

[Back to top ⇧](#table-of-contents)

***

## Manual Testing

### Common Elements Testing
Manual testing was conducted on the following elements that appear on every page:

- Clicking the Logo located on the top-left of the screen will redirect the user back to the **Home Page**:

    ![Logo Click](static/images/testing-files/manual/logo-click.gif)

- Hovering over the **Navigation Links** will trigger the hover effect, confirming the page the user is on:

    ![Navigation Bar Hover class](static/images/testing-files/manual/nav-hover.gif)

- Collapsible `hamburger` button on mobile and tablet devices reveals **Navigation** menu:

    ![Collapsible Navigation Bar](static/images/testing-files/manual/nav-mob.gif)

- Hovering over the **Footer** icons will trigger the hover effect, confirming the action the user is about to take:
    
    ![Footer Hover class](static/images/testing-files/manual/footer-hover.gif)

- Clicking the **Footer Social Icons** opens the Developers social platform in a new tab:

    - **GitHub:**
    ![Github Link](static/images/testing-files/manual/github.gif)

    - **LinkedIn:**
    ![LinkedIn Link](static/images/testing-files/manual/linkedin.gif)

- Clicking the **Footer Contact Icon** opens the contact modal, with the appropriate user feedback:

    ![Contact Form](static/images/testing-files/manual/contact.gif)

- Clicking the **Disclaimer** icon triggers the disclaimer notice: 

    ![Disclaimer](static/images/testing-files/manual/disclaimer.gif)

- The user can log out from numerous points:

    - My Recipes:

        ![Log out @ My Recipes](static/images/testing-files/manual/lo-recipes.gif)
    
    - My Favourites:

        ![Log out @ My Favourites](static/images/testing-files/manual/lo-faves.gif)
    
    - Quick Links:

        ![Log out @ Quick Links](static/images/testing-files/manual/lo-quicklink.gif)
    
    - On Mobile Devices:

        ![Log out on mobile](static/images/testing-files/manual/lo-mobile.gif)

- Recipes can be accessed by clicking:

    - Image

        ![Recipe Image Click](static/images/testing-files/manual/recipe-img.gif)

    - Name

        ![Recipe Image Name](static/images/testing-files/manual/recipe-name.gif)

### Page Elements Testing

#### Home Page

Manual testing was conducted on the following elements on the **Home** Page:

- Using the **Carousel Controls**, the user can browse the featured recipes (the last four to be uploaded):

    ![Carousel Controls](static/images/testing-files/manual/carousel.gif)

- Hovering over the **Call to Action** buttons will provide feedback to the user: 

    ![Home Page Buttons](static/images/testing-files/manual/home-btns.gif)

- The Responsiveness of the **Home Page**:

    ![Home Page Responsiveness](static/images/testing-files/manual/home-res.gif)

#### Find A Recipe Page

Manual testing was conducted on the following elements on the **Find A Recipe** Page:

- The Search Bar allows users to enter their search query:

    - When Results are found:
    
        ![Search Results](static/images/testing-files/manual/search-results.gif)

    - No Results Found:
    
        ![No Search Results](static/images/testing-files/manual/search-no-results.gif)

- The **Dropdown** Menus allow the user to filter their search:

    - Category Search:
    
        ![Category Filter Search](static/images/testing-files/manual/category.gif)

    - Difficulty Search:
    
        ![Level Filter Search](static/images/testing-files/manual/level.gif)

- The **Pagination** function only displays 6 recipes at a time, allowing the user to browse through pages without suffering from information-overload:

    ![Pagination](static/images/testing-files/manual/paginate.gif)

- The Responsiveness of the **Find A Recipe Page**:

    ![Find A Recipe Responsiveness](static/images/testing-files/manual/search-res.gif)

#### Sign Up Page

Manual testing was conducted on the following elements on the **Sign Up** Page:

- User can intuitively create an account: 

    ![Registration Process](static/images/testing-files/manual/register.gif)

- Clicking **Login** redirects user to login page:

    ![Sign Up to Log in](static/images/testing-files/manual/reg-log.gif)

- The Responsiveness of the **Sign Up Page**:

    ![Sign Up Page Responsiveness](static/images/testing-files/manual/register-res.gif)

#### Login Page

Manual testing was conducted on the following elements on the **Login** Page:

- User can intuitively enter their details to log into their account:

    ![Login Process](static/images/testing-files/manual/login.gif)

- Clicking **Sign Up** redirects user to registration page:

    ![Log in to Sign Up](static/images/testing-files/manual/log-reg.gif)

- The Responsiveness of the **Login Page**:

    ![Login Page Responsiveness](static/images/testing-files/manual/login-res.gif)

#### My Recipes Page

Manual testing was conducted on the following elements on the **My Recipes** Page:

- Hovering over **Call to Action** buttons provide user feedback: 

    ![My Recipes buttons hover class](static/images/testing-files/manual/recipe-btns.gif)

- The Responsiveness of the **My Recipes Page**:

    ![My Recipes Responsiveness](static/images/testing-files/manual/myrecipes-res.gif)

#### My Favourites Page

Manual testing was conducted on the following elements on the **My Favourites** Page:

- Hovering over **Call to Action** buttons provide user feedback: 

    ![My Recipes buttons hover class](static/images/testing-files/manual/fave-btns.gif)

- The Responsiveness of the **My Favourites Page**:

    ![My Recipes Responsiveness](static/images/testing-files/manual/faves-res.gif)

#### Edit User Page

Manual testing was conducted on the following elements on the **Edit User** Page:

- User can intuitively edit their profile: 
    
    ![Edit User Process](static/images/testing-files/manual/edit-user.gif)

- Clicking **Cancel** redirects user to My Recipes page:

    ![Edit User - Cancel button](static/images/testing-files/manual/edit-user-cancel.gif)

- The Responsiveness of the **Edit User Page**:

    ![Edit User Page Responsiveness](static/images/testing-files/manual/edit-user-res.gif)

#### Edit Accounts Page

Manual testing was conducted on the following elements on the **Edit Accounts** Page:

- User can intuitively edit their account:

    ![Edit Account Process](static/images/testing-files/manual/edit-acc.gif)

- Clicking **Back** redirects user to Edit Profile page:

    ![Edit Account - Back button](static/images/testing-files/manual/edit-acc-back.gif)

- Clicking **Delete Account** opens **Delete Modal**:

    ![Delete Account Modal](static/images/testing-files/manual/delete-acc.gif)

- The Responsiveness of the **Edit Accounts Page**:

    ![Edit Account Page Responsiveness](static/images/testing-files/manual/edit-acc-res.gif)

#### Create Recipe Page

Manual testing was conducted on the following elements on the **Create Recipe** Page:

- The creative process for entering recipe details is as follows:
    
    - Enter Recipe name

        ![Enter Recipe Name](static/images/testing-files/manual/create-name.gif)

    - Enter image url, an image preview will be displayed:
    
        ![Enter Recipe Img URL](static/images/testing-files/manual/create-img.gif)

    - User can use **Dropdown** menus to refine recipe:

        ![Refine Recipe by Dropdowns](static/images/testing-files/manual/create-dropdown.gif)

    - Add and remove ingredients **dynamically**:

        ![Add and Remove Ingredients](static/images/testing-files/manual/create-ingred.gif)

    - Add and remove directions **dynamically**:

        ![Add and Remove Directions](static/images/testing-files/manual/create-direct.gif)

- Clicking **Save** will redirect the user to My Recipes page: 

    ![Click Save](static/images/testing-files/manual/create-save.gif)

- Clicking **Cancel** will return the user back to the previous page: 

    ![Click Cancel](static/images/testing-files/manual/create-cancel.gif)

- The Responsiveness of the **Create Recipe Page**:

    ![Create Recipe Page Responsiveness](static/images/testing-files/manual/create-res.gif)

#### Edit Recipe Page

Manual testing was conducted on the following elements on the **Edit Recipe** Page:

- Current information will be the default value, User can edit as needed:

    ![Edit Recipe Process](static/images/testing-files/manual/edit-rec.gif)

- Clicking **Cancel** will return the user back to the recipe page: 

    ![Edit Recipe Cancel button](static/images/testing-files/manual/edit-cancel.gif)

- Clicking **Delete** opens **Delete Modal**:

    ![Edit Recipe Delete Modal](static/images/testing-files/manual/edit-delete.gif)

- The Responsiveness of the **Edit Recipe Page**:

    ![Edit Recipe Page Responsiveness ](static/images/testing-files/manual/edit-rec-res.gif)
 
#### Recipe Page

Manual testing was conducted on the following elements on the **Recipe** Page:

- Clicking the **Back** button will return the user to the previous page: 

    ![Recipe Page Back button](static/images/testing-files/manual/rec-back.gif)

- If the user is not logged in, the **Login To Add Favourites** Button will redirect them to the **Login** page: 

    ![Non-User on Recipe Page](static/images/testing-files/manual/rec-non.gif)

- If the user is **not** the recipe author, they can add the recipe to, or remove it from their Favourites:

    ![Not Author on Recipe Page](static/images/testing-files/manual/rec-user.gif)

- If the user **is** the author, they can edit or delete the recipe:

    ![Author on Recipe Page](static/images/testing-files/manual/rec-auth.gif)

    - **Edit** directs to **Edit Recipe Page**:
    
        ![Recipe to Edit Recipe](static/images/testing-files/manual/rec-edit.gif)

    - **Delete** opens the **Delete Modal**:
    
        ![Recipe Delete Modal](static/images/testing-files/manual/rec-delete.gif)

- The Responsiveness of the **Recipe Page**:

    ![Recipe Page Responsiveness](static/images/testing-files/manual/rec-res.gif)


[Back to top ⇧](#table-of-contents)

***

## Automated Testing

### Code Validation

- [W3C Markup Validator](https://validator.w3.org/ "Link to W3C Markup Validator") was used to validate the `HTML` code used, using the `Validate by URI` method.

    - All errors that were highlighted were resolved.

-  [W3C CSS Validator](https://jigsaw.w3.org/css-validator/ "Link to W3C CSS Validator") was used to validate the `CSS` code used with the following result:

    ![Style sheet validation results](static/images/testing-files/automated/css-val.png)


- [JSHint](https://jshint.com/ "Link to JSHint") was used to validate the `JavaScript` and `JQuery` code used.

    - Errors highlighted in `script.js` pertain to [SweetAlert2](https://sweetalert2.github.io/ "Link to Sweet Alert 2 page") (used for contact form feedback) and [jQuery Validation](https://jqueryvalidation.org/ "Link to jQuery Validation page")(used for validating contact form) as well as the `onclick` functions used for image preview and disclaimer:

        ![Script Validation Results](static/images/testing-files/automated/js-val.png) 


    - There were no errors highlighted in `recipe.js` file

- [PEP8 Online](http://pep8online.com/ "Link to PEP8 Online") was used to validate `Python` code.
    
    - All highlighted errors and warnings were resolved.

### Browser Validation
**Chrome:**

![Chrome test image](static/images/testing-files/automated/chrome.png)

**Safari:**

![Safari test image](static/images/testing-files/automated/safari.png)

**Edge:**

![Edge test image](static/images/testing-files/automated/edge.png)


**Opera:**

![Opera test image](static/images/testing-files/automated/opera.png)

**Firefox:**

![Firefox test image](static/images/testing-files/automated/firefox.png)

### Lighthouse Auditing

#### Desktop
| Page | Performance | Accessibility | Best Practice | SEO |
|------|:-------------:|:---------------:|:---------------:|:-----:|
| Home Page | 86% | 100% | 80% | 100% |
| Find Recipes | 99% | 92% | 80% | 90% |
| Login | 97% | 100% | 80% | 100% |
| Register | 99% | 100% | 80% | 100% |
| Edit User | 99% | 100% | 80% | 100% |
| Edit Account | 99% | 100% | 80% | 100% |
| My Recipes | 97% | 100% | 80% | 100% |
| My Favourites | 98% | 100% | 80% | 90% |
| Create Recipe | 99% | 100% | 80% | 100% |
| Edit Recipe | 98% | 90% | 80% | 100% |
| Recipe Page | 96% | 100% | 80% | 90% |

#### Mobile
| Page | Performance | Accessibility | Best Practice | SEO |
|------|:-------------:|:---------------:|:---------------:|:-----:|
| Home Page | 86% | 100% | 93% | 100% |
| Find Recipes | 73% | 92% | 93% | 90% |
| Login | 93% | 100% | 87% | 100% |
| Register | 92% | 100% | 87% | 100% |
| Edit User | 70% | 100% | 87% | 100% |
| Edit Account | 92% | 100% | 87% | 100% |
| My Recipes | 79% | 100% | 93% | 100% |
| My Favourites | 89% | 100% | 93% | 90% |
| Create Recipe | 92% | 100% | 87% | 100% |
| Edit Recipe | 82% | 90% | 87% | 100% |
| Recipe Page | 74% | 100% | 87% | 92% |

#### Breakdown of Results

| Page | Error / Warning | Comment |
|:-----:|:---------------:|:-------|
| All Pages | Largest Contentful Paint | The images rendered on each page threw this error due to a number of reasons. The developer was able to pre-load their **own** images rendered using the `rel="preload"` attribute in **HTML** and using `-webkit-image-set()` in **CSS** ([Source](https://web.dev/preload-responsive-images/)). The problem still persists due to the use of third party images throughout the site.|
| All Pages | Render-blocking resources | This warning stems from the use of `emailJS` for the contact form. The developer attempted to resolve this issue using the `defer` attribute within the script tag, but this only created an issue whereby the function sending the email was not called. |
| Home Page | Tap targets not sized appropriately | Relating to the carousel controls. Issue was resolved by resizing the anchor tag of the controls. |
| Home Page | Defer offscreen images | This relates to the carousel feature of the home page. The researched solution was to 'lazy-load' the images but that is not an option in this release due to the use of image urls, in lieu of uploads. |
| My Favourites | Links are not crawlable | Relating to the `.page-link` class in the Bootstrap Pagination controls. |
| All Pages | Avoid enormous network payload | This warning relates to the use of external images throughout the site. The payload size fluctuated significantly because of this. The solution to this would be to upload images directly to the site, but this feature is not included in this release |
| Find Recipes | Size Images | This issue (like many others before) pertains to the use of external images, where the resource size is far greater than the displayed size. |
| All Pages | Does not use HTTPS | In researching this error, the only conclusive reason for it is the use of mixed content throughout the site. |


[Back to top ⇧](#table-of-contents)

***

## User testing 
Family members and friends were asked to review the site and documentation to point out any bugs and/or user experience issues. Their helpful advice throughout the process led to many UX changes in order to create a better experience. 

| It was through this testing that the following changes were made:|
|-----------------------|
| Update to Logo to be more conventionally positioned. The original designs were for a floating logo but that was quickly replaced due to the issues it caused (most notable `padding` and `z-index` errors).|
| Change to Recipe Card `font-size` and `max-length` in order to create consistency across all recipes. It was noted that some of the recipe names were longer than others, creating a spacing issue, taking away from the User Experience.|
| Create conditional buttons for each category in order to better distinguish the differences, giving these graphical cues helped users to visual the category.|
| Create a 'quick-links' function for users to create a more streamline experience. |
| Create a separate **Accounts Settings** page just for changing password or deleting account, in order to avoid the "danger" zone as much as possible. |
| Create a live image preview window, allowing the user to see the current image on the **Edit User** and **Edit Recipe** pages.|
| A **breadcrumbs** button on the Recipe page, allowing the users to return to their previous page for convenience.|
| Create a *Search Again* button on the **Find Recipes** search results in order to provide the user with easy return access.|

[Back to top ⇧](#table-of-contents)

***

## Note to Accessor
If you would like to log in, to gain access to the full functionality of the site, a *test* account has been created *(login information provided in Project Submission)*. This account has recipes already created and favourited, for your convenience.

The developer recommends that you create your own account in order to get the complete experience in using the site. A [Recipes](recipe-example.md) File has been created for you to copy and paste a recipe to get the **Creating a Recipe** experience (without having to search the internet).

***

[Back to top ⇧](#table-of-contents)