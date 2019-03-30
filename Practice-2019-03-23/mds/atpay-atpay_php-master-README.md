# @Pay PHP Bindings

PHP implementation of @Pay's [**Token Protocol**](http://developer.atpay.com/v3/tokens/protocol/). See the [@Pay Developer Site](http://developer.atpay.com/)
for additional information.

A **Token** is a value that contains information about a financial transaction (an invoice
or a product sales offer, for instance). When a **Token** is sent to
`transaction@processor.atpay.com` from an address associated with a **Payment Method**,
it will create a **Transaction**.

There are two classes of **Token** @Pay processes - the **Targeted Token**, which should
be used for sending invoices or transactions applicable to a single
recipient, and the **Bulk Token**, which is suitable for email marketing lists.

An **Email Button** is a link embedded in an email message. When activated, this link
opens a new outgoing email with a recipient, subject, and message body
prefilled. By default this email contains one of the two token types. Clicking
'Send' delivers the email to @Pay and triggers **Transaction** processing. The sender will
receive a receipt or further instructions.

## Installation

*This library requires that the [PHP Sodium](https://github.com/alethia7/php-sodium) Extension be installed.*

### PHP Archive

```bash
$ curl -O -L http://github.com/atpay/atpay_php/releases/download/2.0.2/atpay_php.phar
```

Then require `atpay_php` in your application:

```php
require_once 'atpay_php.phar';        # include php archive.
```

### Composer

```json
{
  "require": {
    "atpay/atpay_php": "2.0.5"
  }
}
```

```
$ curl -s http://getcomposer.org/installer | php
$ php composer.phar install
```

```php
require 'vendor/autoload.php';
```

## Configuration

All Token generation functions require a Session object. Grab your API credentials from https://dashboard.atpay.com/ (API Settings):

```php
$session = new \AtPay\Session(partner_id, public_key, private_key);
```

## Targeted Tokens

A **targeted** token is ideal for sending invoices or for transactions that are
only applicable to a single recipient (specialized offers, etc).

The following creates a token for a 20 dollar transaction specifically for the
credit card @Pay has associated with 'test@example.com':

```php
$invoice_token = new \AtPay\Token\Targeted($session, 20, 'customer@example.com');
echo $invoice_token->to_s();
```
Note: **Targeted** tokens used to be known as **Invoice** tokens. Please use **Targeted** tokens, as **Invoice** tokens will be deprecated.


## Bulk Tokens

Most merchants will be fine generating **Bulk Email Buttons** manually on the [@Pay Merchant
Dashboard](https://dashboard.atpay.com), but for cases where you need to
automate the generation of these messages, you can create **Bulk Tokens** without
communicating directly with @Pay's servers.

A **Bulk Token** is designed for large mailing lists. You can send the same token
to any number of recipients. It's ideal for 'deal of the day' type offers, or
general marketing.

To create a **Bulk Token** for a 30 dollar blender:

```php
$bulk_token = new \AtPay\Token\Bulk($session, 30);
echo $bulk_token->to_s();
```

If a recipient of this token attempts to purchase the product via email but
hasn't configured a credit card, they'll receive a message asking them to
complete their transaction. You should integrate the @Pay JS SDK on that page
if you want to allow them to create
a two-click email transaction in the future.

## General Token Attributes

### Auth Only

A **Token** will trigger a funds authorization and a funds capture
simultaneously. If you're shipping a physical good, or for some other reason
want to delay the capture, use the `auth_only!` method to adjust this behavior:

```php
$invoice_token = new \AtPay\Token\Targeted($session, 20, 'customer@example.com');
$invoice_token->auth_only();
echo $invoice_token->to_s();
```

### Expiration

A **Token** expires in 2 weeks unless otherwise specified. Trying to use the **Token**
after the expiration results in a polite error message being sent to the sender.
To adjust the expiration:

```php
$invoice_token = new \AtPay\Token\Targeted($session, 20, 'customer@example.com');
$invoice_token->expires_in_seconds(60 * 60 * 24 * 7); // one week
echo $invoice_token->to_s();
 ```

### Signup Page

When a new Customer or a Customer with expired or invalid credit card details
attempts to purchase from an Email, they will be redirected to a Token's **Signup Page**,
where they can enter new Credit Card details. By default @Pay will host the
**Signup Page**, but you may wish to direct the Customer to a product page on
your own site (Enable @Pay Card tokenization on your own page with the
[@Pay JS SDK](http://developer.atpay.com/v3/javascript/)). To specify a custom
URL:

```php
$invoice_token = new \AtPay\Token\Targeted($session, 20, 'test@example.com');
$invoice_token->url('https://example.com/invoices/123');
echo $invoice_token->to_s();
 ```

#### Requesting Custom Information on a Hosted Signup Page

If you opt to use the **Hosted Payment Capture Page** (by not specifying a URL above), you
can request further information from your Customer during the purchase on the
Web. For instance, the following requests an optional Gift Message:

```php
$invoice_token = new \AtPay\Token\Targeted($session, 20, 'test@example.com');
$invoice_token->request_custom_data('gift_message', true); //Input name , required (defaults to false)
echo $invoice_token->to_s();
 ```


#### Requesting the URL of a Hosted Signup Page

The **Hosted Payment Capture Page** is related directly to a Token. It is
created when the token is first received at `transaction@processor.atpay.com` or
when the URL is requested from @Pay prior to the first use. To request the URL, you
must contact @Pay's server:

```php
$invoice_token = new \AtPay\Token\Targeted($session, 20, 'test@example.com');
$registration = $invoice_token->register();

echo $registration->url();
=> "https://example.secured.atpay.com/{token_identifier}"

echo $registration->short();
=> "atpay://{token_identifier}"
```

NOTE: For high traffic this solution may be inadequate. Contact @Pay for
consultation.




#### Item Name

You can set an **item name** that will display on the **Hosted Payment Capture Page**

```php
$invoice_token = new \AtPay\Token\Targeted($session, 20, 'test@example.com');
$invoice_token->name("A Cool Offer");
echo $invoice_token->to_s();
 ```

#### Item Details

You can set an **item details** that will display on the **Hosted Payment Capture Page**

```php
$invoice_token = new \AtPay\Token\Targeted($session, 20, 'test@example.com');
$invoice_token->set_item_details("Lorem Ipsum ...");
echo $invoice_token->to_s();
 ```

#### Address Collection

Request the **Hosted Payment Capture Page** collect any combination
of shipping or billing address with `requires_shipping_address(true)` and
`requires_billing_address(true)`:

```
$invoice_token = new \AtPay\Token\Targeted($session, 20, 'test@example.com');
$invoice_token->requires_billing_address(true);
$invoice_token->requires_shipping_address(true);
echo $invoice_token->to_s();
```

### Set Item Quantity

If you are using @Pay's webhook for inventory control, you can specify an initial quantity for the offer you are creating.

```php
$invoice_token = new \AtPay\Token\Targeted($session, 20, 'test@example.com');
$invoice_token->set_item_quantity(3);
echo $invoice_token->to_s();
 ```

### Fulfillment Time

**Transaction Details** from @Pay may include an **Estimated Fulfillment Time**.
@Pay expects **Auth Only** transactions when fulfillment is required.
A Transaction should be Captured only when fulfillment is completed.

```php
$invoice_token = new \AtPay\Token\Targeted($session, 20, 'test@example.com');
$token_token->estimated_fulfillment_days(3)      # The token is now auth-only!
email(token.to_s, receipient_address)
```

### Custom User Data

**Custom User Data** is a token attribute that contains any string that you wish to get back in @Pay’s
response on processing the token. It has a limit of 2500 characters.

```php
$invoice_token = new \AtPay\Token\Targeted($session, 20, 'customer@example.com');
$invoice_token->custom_user_data("{foo => bar}");
echo $invoice_token->to_s();
```

## Button Generation

The PHP client does not currently support button generation.

## Full Example

```php
<?php
  // Include @Pay's PHP SDK
  require_once 'atpay_php.phar';        # include php archive.
  //require 'vendor/autoload.php';      # when using composer.

  // Configure with your keys:
  $partner_id       = '';
  $public_key       = '';
  $private_key      = '';

  $session = new \AtPay\Session($partner_id, $public_key, $private_key);

  // Generate a new Invoice Token for $150
  $total_price    = 150;
  $customer_email = "customer@example.com";


  $invoice_token = new \AtPay\Token\Targeted($session, $total_price, $customer_email);
  $token         = $invoice_token->to_s();

  // Send an Email to the Customer
  $subject = "You Abandoned Your Cart!";
  $from    = "merchant@example.com";

  $headers  = 'MIME-Version: 1.0' . "\r\n";
  $headers .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";
  $headers .= 'From: '.$from."\r\n";
  $message  = '<a href="mailto:transaction@processor.atpay.com?subject='.urlencode('PHP Token').'&body='.urlencode($token).'">Click to Buy</a>'; # creates a mailto with generated invoice token that will send to @Pay to process

  // Send the email
  mail($customer_email, $subject, $message, $headers);

  // Done
  echo "Invoice Sent!";
?>
```

