# pland — Command-Referenz (generiert)

## absences

| Command | Methode | Beschreibung |
|---|---|---|
| `pland absences approve` | POST | Approve absence |
| `pland absences approve-multiple` | POST | Approve multiple absences |
| `pland absences assign-replacements` | POST | Assign absence replacements |
| `pland absences calc-active-for-every-day-in-range` | GET | Calculate absence capacity by date range |
| `pland absences cancel` | POST | Cancel absence |
| `pland absences create` | POST | Create new absence |
| `pland absences decline` | POST | Decline absence |
| `pland absences delete` | DELETE | Delete absence |
| `pland absences get` | GET | Get absence by ID |
| `pland absences get-affected-jobs` | GET | Get absence affected jobs |
| `pland absences get-replacement-jobs` | GET | Get absence replacement jobs |
| `pland absences get-user-days-absent` | GET | Get user days absent |
| `pland absences get-user-vacation-days` | GET | Get user vacation days |
| `pland absences has-in-time-frame` | GET | Check for conflicting absences |
| `pland absences list` | GET | List absences |
| `pland absences list-personal` | GET | List personal absences |
| `pland absences list-requestable-types` | GET | List requestable absence types |
| `pland absences update` | PATCH | Update absence |
| `pland absences update-full` | PUT | Update absence (full) |

## activity-types

| Command | Methode | Beschreibung |
|---|---|---|
| `pland activity-types create` | POST | Create activity type |
| `pland activity-types create-with-assignment` | POST | Create activity type with assignment |
| `pland activity-types delete` | DELETE | Delete activity type |
| `pland activity-types get` | GET | Get activity type |
| `pland activity-types list` | GET | List activity types |
| `pland activity-types update` | PATCH | Update activity type |

## api-keys

| Command | Methode | Beschreibung |
|---|---|---|
| `pland api-keys create-api-key` | POST | Create API Key |
| `pland api-keys delete-api-key` | DELETE | Expire API Key |
| `pland api-keys get-api-key` | GET | List API Keys |
| `pland api-keys update-api-key` | PATCH | Rotate API Key |

## articles

| Command | Methode | Beschreibung |
|---|---|---|
| `pland articles become-default` | POST | Set article as default for a budget |
| `pland articles create-custom` | POST | Create a new article (custom logic) |
| `pland articles delete` | DELETE | Delete article |
| `pland articles get` | GET | Get article by ID |
| `pland articles get-distinct-values-custom` | GET | Get distinct values for articles (custom) |
| `pland articles get-last-number` | GET | Get last article number |
| `pland articles is-default` | GET | Check if article is default |
| `pland articles list` | GET | List all articles |
| `pland articles list-all-for-user` | GET | List all articles for a user |
| `pland articles list-objects-for` | GET | List objects for an article |
| `pland articles order-material` | POST | Order material for an object |
| `pland articles remove-default` | DELETE | Remove article as default |
| `pland articles update` | PATCH | Update article |
| `pland articles update-amount-in-stock` | PATCH | Update amount in stock for multiple articles |

## assets

| Command | Methode | Beschreibung |
|---|---|---|
| `pland assets redirect-to-secure` | GET | Get secure asset URL |

## assignment-confirmations

| Command | Methode | Beschreibung |
|---|---|---|
| `pland assignment-confirmations add-documents-to` | POST | Add new documents |
| `pland assignment-confirmations attach-documents-to` | POST | Attach documents |
| `pland assignment-confirmations create-preview` | POST | Create assignment confirmation preview |
| `pland assignment-confirmations delete` | DELETE | Delete assignment confirmation |
| `pland assignment-confirmations generate-combined-pdf` | POST | Generate combined PDF |
| `pland assignment-confirmations generate-single-pdf` | POST | Generate PDF for assignment confirmation |
| `pland assignment-confirmations get` | GET | Get assignment confirmation by ID |
| `pland assignment-confirmations list-referenced-documents` | GET | List referenced documents |
| `pland assignment-confirmations send` | POST | Send assignment confirmations |

## assignments

| Command | Methode | Beschreibung |
|---|---|---|
| `pland assignments calculate-capacities` | POST | Calculate assignment capacities |
| `pland assignments calculate-covers` | POST | Calculate assignment coverage |
| `pland assignments count-with-filter` | GET | Count assignments with filter |
| `pland assignments create-invoices-for` | POST | Create invoices for assignments |
| `pland assignments create-service-reports-for` | POST | Create service reports for assignments |
| `pland assignments delete` | DELETE | Delete assignment |
| `pland assignments duplicate` | POST | Duplicate assignments |
| `pland assignments generate-recurring-invoices` | POST | Generate recurring invoices (Debug) |
| `pland assignments get-distinct-field-values` | GET | Get distinct field values |
| `pland assignments get-last-number` | GET | Get last assignment number |
| `pland assignments get-next-invoice-date-preview` | POST | Preview next invoice dates |
| `pland assignments get-or-create-chat` | POST | Get or create assignment chat |
| `pland assignments get-partial-invoices-for` | GET | Get partial invoices for assignment |
| `pland assignments get-user` | GET | Get user assignments |
| `pland assignments list` | GET | List assignments |
| `pland assignments realize-dynamic-positions` | POST | Realize dynamic positions |
| `pland assignments set-end-date` | POST | Set assignment and jobs end date |
| `pland assignments update` | PATCH | Update assignment |
| `pland assignments update-many` | PATCH | Update multiple assignments |
| `pland assignments update-product-prices` | PATCH | Update product prices |
| `pland assignments view` | GET | Get assignment by ID |

## authentication

| Command | Methode | Beschreibung |
|---|---|---|
| `pland authentication create-auth-using-sms` | POST | SMS Authentication |
| `pland authentication create-change-password` | POST | Change Password |
| `pland authentication create-login` | POST | User Login |
| `pland authentication create-password` | POST | Reset Password Request |
| `pland authentication create-request-auth-code` | POST | Request SMS Authentication Code |
| `pland authentication create-set` | POST | Set New Password with Token |

## banking-transactions

| Command | Methode | Beschreibung |
|---|---|---|
| `pland banking-transactions create` | POST | Create banking transaction |
| `pland banking-transactions delete` | DELETE | Delete banking transaction |
| `pland banking-transactions delete-many` | POST | Delete multiple transactions |
| `pland banking-transactions get-distinct-values` | GET | Get distinct values |
| `pland banking-transactions get-matching-invoices` | GET | Get matching invoices for transaction |
| `pland banking-transactions ignore` | POST | Ignore/unignore transactions |
| `pland banking-transactions list` | GET | List banking transactions |
| `pland banking-transactions list-senders` | GET | List transaction senders |
| `pland banking-transactions match-to-invoices` | POST | Match transaction to invoices |
| `pland banking-transactions unmatch` | POST | Unmatch transaction from invoices |

## chat-legacy

| Command | Methode | Beschreibung |
|---|---|---|
| `pland chat-legacy add-channel-members` | POST | Add channel members |
| `pland chat-legacy create-channel` | POST | Create chat channel |
| `pland chat-legacy delete-channel` | DELETE | Delete chat channel |
| `pland chat-legacy get-user-token` | GET | Get chat user token |
| `pland chat-legacy remove-channel-members` | POST | Remove channel members |
| `pland chat-legacy send-invite-sms` | POST | Send chat invite SMS |
| `pland chat-legacy update-channel` | POST | Update chat channel |

## client

| Command | Methode | Beschreibung |
|---|---|---|
| `pland client accept-offer` | GET | Accept offer |
| `pland client create-unauthorized-complain` | POST | Create complaint |
| `pland client create-unauthorized-task` | POST | Create task |
| `pland client create-user-unauthorized` | POST | Create user (unauthorized) |
| `pland client decline-offer` | GET | Decline offer |
| `pland client get-company-info-unauthorized` | GET | Get company info |
| `pland client get-credit` | GET | Get credit document |
| `pland client get-invoice` | GET | Get invoice document |
| `pland client get-object-documentation` | GET | Get object documentation |
| `pland client get-offer` | GET | Get offer document |
| `pland client update-user-unauthorized` | POST | Update user (unauthorized) |
| `pland client upload-documents` | POST | Upload documents |
| `pland client upload-to-complaint` | POST | Upload complaint image |

## company

| Command | Methode | Beschreibung |
|---|---|---|
| `pland company consent-to-bank-integration` | POST | Consent to bank integration |
| `pland company disable-custom-email-settings` | POST | Disable custom email settings |
| `pland company get-info` | GET | Get company information |
| `pland company set-custom-email-settings` | POST | Set custom email settings |
| `pland company set-info` | PATCH | Set company info |
| `pland company set-logo` | POST | Set company logo |
| `pland company update` | PATCH | Update company |

## complaints

| Command | Methode | Beschreibung |
|---|---|---|
| `pland complaints assign` | POST | Assign complaint to user |
| `pland complaints count` | GET | Count complaints |
| `pland complaints count-new` | GET | Count new complaints |
| `pland complaints count-user` | GET | Count user complaints |
| `pland complaints create` | POST | Create complaint |
| `pland complaints delete` | DELETE | Delete complaint |
| `pland complaints generate-response` | GET | Generate AI response for complaint |
| `pland complaints get` | GET | Get complaint by ID |
| `pland complaints get-distinct-values` | GET | Get complaint distinct values |
| `pland complaints get-generations-left` | GET | Get remaining AI generations |
| `pland complaints get-monitor` | GET | Get complaint monitor data |
| `pland complaints get-user` | GET | Get user complaints |
| `pland complaints list` | GET | List complaints |
| `pland complaints resolve` | POST | Resolve complaint |
| `pland complaints update` | PATCH | Update complaint |

## contacts

| Command | Methode | Beschreibung |
|---|---|---|
| `pland contacts create` | POST | Create contact |
| `pland contacts delete` | DELETE | Delete contact |
| `pland contacts get` | GET | Get contact |
| `pland contacts get-distinct-values` | GET | Get distinct values |
| `pland contacts list` | GET | List contacts |
| `pland contacts list-for-object` | GET | List contacts for object |
| `pland contacts list-job` | GET | List job contacts |
| `pland contacts update` | PATCH | Update contact |
| `pland contacts update-many` | PATCH | Batch update contacts |

## credit

| Command | Methode | Beschreibung |
|---|---|---|
| `pland credit add-documents-to` | POST | Add documents to credit note |
| `pland credit attach-documents-to` | POST | Attach documents to credit note |
| `pland credit create` | POST | Create credit note |
| `pland credit create-preview` | POST | Create credit note preview |
| `pland credit delete` | DELETE | Delete credit note |
| `pland credit duplicate` | POST | Duplicate credit note |
| `pland credit generate-combined-pdf` | POST | Generate combined credit PDF |
| `pland credit generate-pdf` | POST | Generate credit note PDF |
| `pland credit generate-zip` | POST | Generate credit ZIP archive |
| `pland credit get` | GET | Get credit note |
| `pland credit get-count` | GET | Get credit count |
| `pland credit get-distinct-values` | GET | Get distinct field values |
| `pland credit get-last-number` | GET | Get last credit number |
| `pland credit get-or-create-chat` | POST | Get or create credit note chat |
| `pland credit list` | GET | List credit notes |
| `pland credit list-referenced-faktura-documents-from` | GET | List referenced faktura documents |
| `pland credit send` | POST | Send credit notes |
| `pland credit set-fixed` | POST | Set credit notes to fixed |
| `pland credit update` | PATCH | Update credit note |

## customer-objects

| Command | Methode | Beschreibung |
|---|---|---|
| `pland customer-objects add-material` | POST | Add material to object |
| `pland customer-objects change-material-budget` | PATCH | Change material budget |
| `pland customer-objects count` | GET | Count customer objects |
| `pland customer-objects create` | POST | Create customer object |
| `pland customer-objects delete` | DELETE | Delete customer object |
| `pland customer-objects get` | GET | Get customer object by ID |
| `pland customer-objects get-assigned-managers` | GET | Get assigned object managers |
| `pland customer-objects get-available-tags` | GET | Get available object tags |
| `pland customer-objects get-basic-assignments-of` | GET | Get object assignments for time tracking |
| `pland customer-objects get-by-number` | GET | Get customer object by number |
| `pland customer-objects get-last-number` | GET | Get last object number |
| `pland customer-objects list` | GET | List customer objects |
| `pland customer-objects list-active-users-on` | GET | List active users on object |
| `pland customer-objects list-by` | GET | List objects by customer |
| `pland customer-objects list-by-location` | GET | List customer objects by location |
| `pland customer-objects list-material` | GET | List object material |
| `pland customer-objects remove-material` | DELETE | Remove material from object |
| `pland customer-objects set-end-date-for-and-assignments` | POST | Set end date for object and assignments |
| `pland customer-objects set-location` | POST | Set object location |
| `pland customer-objects update` | PATCH | Update customer object |

## customers

| Command | Methode | Beschreibung |
|---|---|---|
| `pland customers count` | GET | Count customers |
| `pland customers create` | POST | Create customer |
| `pland customers delete` | DELETE | Delete customer |
| `pland customers get` | GET | Get customer |
| `pland customers get-distinct-values` | GET | Get distinct values |
| `pland customers get-documentation` | GET | Get customer documentation |
| `pland customers get-last-number` | GET | Get last customer number |
| `pland customers get-or-create-chat` | POST | Get/create customer chat |
| `pland customers list` | GET | List customers |
| `pland customers set-end-date` | POST | Set customer end date |
| `pland customers update` | PATCH | Update customer |
| `pland customers update-many` | PATCH | Batch update customers |

## documents

| Command | Methode | Beschreibung |
|---|---|---|
| `pland documents create` | POST | Upload document(s) |
| `pland documents create-with-url` | POST | Create document from URL |
| `pland documents delete` | DELETE | Delete document |
| `pland documents exists` | GET | Check document existence |
| `pland documents get` | GET | Get document by ID |
| `pland documents get-for-entity` | GET | Get documents for an entity |
| `pland documents list-by-ids` | GET | List documents by IDs |
| `pland documents update` | PATCH | Update document |

## equipment

| Command | Methode | Beschreibung |
|---|---|---|
| `pland equipment create` | POST | Create equipment |
| `pland equipment delete` | DELETE | Delete equipment |
| `pland equipment get` | GET | Get equipment |
| `pland equipment get-distinct-values` | GET | Get distinct values |
| `pland equipment get-or-create-chat` | POST | Get/create equipment chat |
| `pland equipment list` | GET | List equipment |
| `pland equipment update` | PATCH | Update equipment |
| `pland equipment update-many` | PATCH | Batch update equipment |

## equipment-types

| Command | Methode | Beschreibung |
|---|---|---|
| `pland equipment-types create` | POST | Create equipment type |
| `pland equipment-types delete` | DELETE | Delete equipment type |
| `pland equipment-types get` | GET | Get equipment type |
| `pland equipment-types get-distinct-values` | GET | Get distinct values |
| `pland equipment-types list` | GET | List equipment types |
| `pland equipment-types update` | PATCH | Update equipment type |

## holiday

| Command | Methode | Beschreibung |
|---|---|---|
| `pland holiday create` | POST | Create holiday |
| `pland holiday delete` | DELETE | Delete holiday |
| `pland holiday import` | POST | Import holidays |
| `pland holiday list` | GET | List holidays |
| `pland holiday update` | PATCH | Update holiday |

## implementation

| Command | Methode | Beschreibung |
|---|---|---|
| `pland implementation get-progress` | GET | Get user implementation progress |

## invoice

| Command | Methode | Beschreibung |
|---|---|---|
| `pland invoice count` | GET | Count invoices |
| `pland invoice create` | POST | Create invoice |
| `pland invoice create-payment-link` | GET | Create payment link for invoice |
| `pland invoice create-stripe-account-link` | GET | Create Stripe account connection link |
| `pland invoice delete` | DELETE | Delete invoice |
| `pland invoice export` | POST | Export invoices |
| `pland invoice generate-multiple-zugferd-pdfs` | POST | Generate ZUGFeRD PDFs for multiple invoices |
| `pland invoice generate-remaining-payments` | POST | Generate remaining payments for invoices |
| `pland invoice generate-single-zugferd-pdf` | POST | Generate ZUGFeRD PDF for invoice |
| `pland invoice generate-xinvoice-xml` | POST | Generate XRechnung XML for invoice |
| `pland invoice get` | GET | Get invoice by ID |
| `pland invoice get-dashboard-data` | POST | Get invoice dashboard data |
| `pland invoice get-distinct-values` | GET | Get distinct field values |
| `pland invoice get-last-number` | GET | Get last invoice number |
| `pland invoice get-transactions` | GET | Get matching transactions for invoice |
| `pland invoice link-to-credit` | POST | Link invoice to credit |
| `pland invoice link-to-reminder` | POST | Link invoice to reminder |
| `pland invoice list` | GET | List invoices |
| `pland invoice send-with-xrechnung` | POST | Send invoices with XRechnung attachments |
| `pland invoice send-with-zugferd` | POST | Send invoices with ZUGFeRD attachments |
| `pland invoice set-canceled` | POST | Cancel invoices |
| `pland invoice set-fixed` | POST | Set invoices to fixed status |
| `pland invoice update` | PATCH | Update invoice |

## invoice-reminder-templates

| Command | Methode | Beschreibung |
|---|---|---|
| `pland invoice-reminder-templates create` | POST | Create invoice reminder template |
| `pland invoice-reminder-templates delete` | DELETE | Delete invoice reminder template |
| `pland invoice-reminder-templates get` | GET | Get invoice reminder template |
| `pland invoice-reminder-templates get-distinct-values` | GET | Get distinct field values |
| `pland invoice-reminder-templates list` | GET | List invoice reminder templates |
| `pland invoice-reminder-templates update` | PATCH | Update invoice reminder template |

## invoice-reminders

| Command | Methode | Beschreibung |
|---|---|---|
| `pland invoice-reminders add-documents-to` | POST | Add documents to reminder |
| `pland invoice-reminders attach-documents-to` | POST | Attach documents to reminder |
| `pland invoice-reminders create` | POST | Create invoice reminder |
| `pland invoice-reminders create-from` | POST | Create reminders from invoices |
| `pland invoice-reminders create-preview` | POST | Create reminder preview |
| `pland invoice-reminders delete` | DELETE | Delete invoice reminder |
| `pland invoice-reminders generate-combined-pdf` | POST | Generate combined PDF for reminders |
| `pland invoice-reminders generate-pdf` | POST | Generate reminder PDF |
| `pland invoice-reminders get` | GET | Get invoice reminder |
| `pland invoice-reminders get-distinct-values` | GET | Get distinct field values for invoice reminders |
| `pland invoice-reminders get-or-create-chat` | POST | Get or create reminder chat |
| `pland invoice-reminders list` | GET | List invoice reminders |
| `pland invoice-reminders list-referenced-faktura-documents-for` | GET | List referenced documents |
| `pland invoice-reminders send` | POST | Send reminders via email |
| `pland invoice-reminders update` | PATCH | Update invoice reminder |

## invoice-storno

| Command | Methode | Beschreibung |
|---|---|---|
| `pland invoice-storno create-add-documents` | POST | Add new documents to storno |
| `pland invoice-storno create-attach-documents` | POST | Attach documents to storno |
| `pland invoice-storno create-pdf` | POST | Generate combined PDF for multiple storno documents |
| `pland invoice-storno create-pdf-by-id` | POST | Generate PDF for specific storno document |
| `pland invoice-storno create-preview` | POST | Create preview of storno document |
| `pland invoice-storno create-send` | POST | Send storno documents via email |
| `pland invoice-storno delete` | DELETE | Delete storno document |
| `pland invoice-storno get` | GET | Get storno document details |
| `pland invoice-storno get-referenced-faktura-documents` | GET | Get referenced documents for storno |
| `pland invoice-storno update` | PATCH | Update storno document |

## invoice-templates

| Command | Methode | Beschreibung |
|---|---|---|
| `pland invoice-templates create` | POST | Create invoice template |
| `pland invoice-templates delete` | DELETE | Delete invoice template |
| `pland invoice-templates get` | GET | Get invoice template |
| `pland invoice-templates get-distinct-values` | GET | Get distinct field values |
| `pland invoice-templates list` | GET | List invoice templates |
| `pland invoice-templates update` | PATCH | Update invoice template |

## jobs

| Command | Methode | Beschreibung |
|---|---|---|
| `pland jobs calculate-target-times-and-allowed-times-for-user-ids` | POST | Calculate user target and allowed times |
| `pland jobs change-accepted-status` | PATCH | Change job accepted status |
| `pland jobs check-user-capacity` | POST | Check user job capacity |
| `pland jobs create` | POST | Create a job |
| `pland jobs delete` | DELETE | Delete a job |
| `pland jobs get-open` | GET | Get open jobs |
| `pland jobs get-status-list-for` | GET | Get job status list |
| `pland jobs get-status-list-for-object` | GET | Get job status list for object |
| `pland jobs get-time-tracking-for` | GET | Get time tracking entries for a job |
| `pland jobs get-user-target-time` | GET | Get user target time |
| `pland jobs in-time-frame` | POST | Get jobs in a specific time frame |
| `pland jobs list` | GET | List all jobs |
| `pland jobs list-by-assignment` | GET | List jobs by assignment |
| `pland jobs list-for-object` | GET | List jobs for object |
| `pland jobs list-for-user` | GET | List jobs for user |
| `pland jobs load-calendar-data` | POST | Load calendar data |
| `pland jobs load-resources-and-calendar-data` | POST | Load resources and calendar data |
| `pland jobs mark-as-started` | POST | Mark job as started |
| `pland jobs patch` | PATCH | Update a job |
| `pland jobs patch-old` | PATCH | Update a job (legacy) |
| `pland jobs view` | GET | Get job by ID |

## logbuch

| Command | Methode | Beschreibung |
|---|---|---|
| `pland logbuch delete-message` | DELETE | Delete a message |
| `pland logbuch get-users-with-access-to-chat` | GET | Get users with access to a chat |
| `pland logbuch list-for-chat` | GET | List messages for chat |
| `pland logbuch mark-messages-as-read` | POST | Mark messages as read |
| `pland logbuch patch-message` | PATCH | Update a message |
| `pland logbuch pin-message` | POST | Pin or unpin a message |
| `pland logbuch send-chat-message` | POST | Send a chat message |
| `pland logbuch send-note-message` | POST | Send a note message |
| `pland logbuch send-thread-message` | POST | Send a thread message |
| `pland logbuch subscribe-users-to-chat` | POST | Subscribe users to a chat |
| `pland logbuch unsubscribe-users-from-chat` | POST | Unsubscribe users from a chat |
| `pland logbuch view-chat` | GET | View chat details |

## material-orders

| Command | Methode | Beschreibung |
|---|---|---|
| `pland material-orders change-budget` | PATCH | Change order items budget or adds article if missing |
| `pland material-orders count` | GET | Count orders |
| `pland material-orders count-new` | GET | Count new orders |
| `pland material-orders delete` | DELETE | Delete order |
| `pland material-orders finish` | PATCH | Mark order as finished |
| `pland material-orders get` | GET | Get order by ID |
| `pland material-orders get-distinct-values` | GET | Get distinct values for orders |
| `pland material-orders get-monitor` | GET | Get order monitor |
| `pland material-orders get-or-create-chat` | POST | Get/create material order chat |
| `pland material-orders get-pdf` | GET | Generate order PDF |
| `pland material-orders list` | GET | List all orders |
| `pland material-orders remove-item` | DELETE | Remove order item |
| `pland material-orders update` | PATCH | Update order |

## notifications

| Command | Methode | Beschreibung |
|---|---|---|
| `pland notifications all-entities-count` | GET | Count all entity types |
| `pland notifications count-user` | GET | Count new notifications |
| `pland notifications get-all` | GET | Get all notifications |
| `pland notifications mark-as-checked` | POST | Mark notification as checked |
| `pland notifications mark-as-read` | POST | Mark notification as read |
| `pland notifications mark-as-un-read` | POST | Mark notification as unread |

## offers

| Command | Methode | Beschreibung |
|---|---|---|
| `pland offers add-documents-to` | POST | Add documents |
| `pland offers attach-documents-to` | POST | Attach documents |
| `pland offers calculate-letter-price` | POST | Calculate letter price |
| `pland offers count` | GET | Count offers |
| `pland offers create` | POST | Create offer |
| `pland offers create-preview` | POST | Create offer preview |
| `pland offers delete` | DELETE | Delete offer |
| `pland offers duplicate` | POST | Duplicate offers |
| `pland offers generate-assignment-confirmations` | POST | Generate assignment confirmations |
| `pland offers generate-combined-pdf` | POST | Generate combined offers PDF |
| `pland offers generate-pdf` | POST | Generate offer PDF |
| `pland offers generate-zip` | POST | Generate offers ZIP |
| `pland offers get` | GET | Get offer by ID |
| `pland offers get-distinct-values` | GET | Get distinct field values |
| `pland offers get-last-number` | GET | Get last offer number |
| `pland offers get-or-create-chat` | POST | Get/create offer chat |
| `pland offers get-partial-invoices-for` | GET | Get partial invoices |
| `pland offers link-to-assignment` | POST | Link offer to assignment |
| `pland offers link-to-invoice` | POST | Link offer to invoice |
| `pland offers list` | GET | List offers |
| `pland offers list-referenced-faktura-documents-for` | GET | List related documents |
| `pland offers send` | POST | Send offers |
| `pland offers send-letters` | POST | Send offer letters |
| `pland offers set-fixed` | POST | Set offers to fixed/open |
| `pland offers set-to-accepted` | POST | Set offers to accepted |
| `pland offers set-to-declined` | POST | Set offers to declined |
| `pland offers update` | PATCH | Update offer |

## pay-types

| Command | Methode | Beschreibung |
|---|---|---|
| `pland pay-types create-absence` | POST | Create absence pay type |
| `pland pay-types create-salary` | POST | Create salary pay type |
| `pland pay-types delete` | DELETE | Delete pay type |
| `pland pay-types get` | GET | Get pay type |
| `pland pay-types get-absences` | GET | List absence pay types |
| `pland pay-types get-salaries` | GET | List salary pay types |
| `pland pay-types update` | PATCH | Update pay type |

## payment-methods

| Command | Methode | Beschreibung |
|---|---|---|
| `pland payment-methods create` | POST | Create payment method |
| `pland payment-methods delete` | DELETE | Delete payment method |
| `pland payment-methods list` | GET | List payment methods |
| `pland payment-methods update` | PATCH | Update payment method |

## payment-terms

| Command | Methode | Beschreibung |
|---|---|---|
| `pland payment-terms create` | POST | Create payment term |
| `pland payment-terms delete` | DELETE | Delete payment term |
| `pland payment-terms get` | GET | Get payment term |
| `pland payment-terms list` | GET | List payment terms |
| `pland payment-terms update` | PATCH | Update payment term |

## payments

| Command | Methode | Beschreibung |
|---|---|---|
| `pland payments create-invoice` | POST | Create payment for invoice |
| `pland payments delete` | DELETE | Delete payment |
| `pland payments get` | GET | List payments |
| `pland payments get-by-id` | GET | Get payment details |
| `pland payments update` | PATCH | Update payment |

## push-notifications

| Command | Methode | Beschreibung |
|---|---|---|
| `pland push-notifications delete` | POST | Delete notifications |
| `pland push-notifications delete-all` | DELETE | Delete all notifications |
| `pland push-notifications delete-all-read` | DELETE | Delete all read notifications |
| `pland push-notifications list` | GET | List notifications |
| `pland push-notifications mark-all-as-read` | POST | Mark all notifications as read |
| `pland push-notifications mark-as-read` | POST | Mark notifications as read |
| `pland push-notifications mark-as-unread` | POST | Mark notifications as unread |

## quality-control

| Command | Methode | Beschreibung |
|---|---|---|
| `pland quality-control create` | POST | Create quality control entry |
| `pland quality-control get` | GET | Get quality control entry |
| `pland quality-control get-monitor` | GET | Get quality control monitoring data |
| `pland quality-control list` | GET | List quality control entries |
| `pland quality-control list-for-object` | GET | List quality control by object |
| `pland quality-control list-for-object-manager` | GET | List quality control by object manager |

## salary

| Command | Methode | Beschreibung |
|---|---|---|
| `pland salary delete` | DELETE | Delete salary |
| `pland salary export-for-objects` | POST | Export salary data for objects |
| `pland salary export-rows` | POST | Export salary rows |
| `pland salary export-rows-in-background` | POST | Export salary rows in background |
| `pland salary get` | GET | Get salary by ID |
| `pland salary get-chat` | POST | Get or create salary chat |
| `pland salary get-groups` | POST | Get salary groups |
| `pland salary get-job-occurrences-without-salaries` | GET | Get job occurrences without salaries |
| `pland salary get-overview-for-objects` | POST | Get salary overview for objects |
| `pland salary get-overview-for-users` | POST | Get salary overview for users |
| `pland salary get-user-absence-salaries` | GET | Get user absence salaries |
| `pland salary get-user-salaries` | GET | Get user salaries |
| `pland salary list-for-object` | GET | List salaries for object |
| `pland salary list-salaries` | GET | List salaries |
| `pland salary release-all-times-in-time-frame` | POST | Release all times in time frame |
| `pland salary release-job-occurrences` | POST | Release job occurrences |
| `pland salary release-using-job` | POST | Release salary using job |
| `pland salary release-using-time-tracking` | POST | Release salary using time tracking |
| `pland salary update` | PATCH | Update salary |

## search

| Command | Methode | Beschreibung |
|---|---|---|
| `pland search perform-global` | GET | Perform Global Search |

## service-products

| Command | Methode | Beschreibung |
|---|---|---|
| `pland service-products count` | GET | Count service products |
| `pland service-products create` | POST | Create a new service product |
| `pland service-products delete` | DELETE | Delete service product |
| `pland service-products get` | GET | Get service product by ID |
| `pland service-products get-distinct-values` | GET | Get distinct values for service products |
| `pland service-products get-last-number` | GET | Get last service product number |
| `pland service-products list` | GET | List all service products |
| `pland service-products update` | PATCH | Update service product |

## service-report

| Command | Methode | Beschreibung |
|---|---|---|
| `pland service-report add-documents-to` | POST | Add documents to service report |
| `pland service-report attach-documents-to` | POST | Attach documents to service report |
| `pland service-report create` | POST | Create service report |
| `pland service-report create-from-app` | POST | Create service report from app |
| `pland service-report create-preview` | POST | Create service report preview |
| `pland service-report delete` | DELETE | Delete service report |
| `pland service-report duplicate` | POST | Duplicate service report |
| `pland service-report generate-combined-pdf` | POST | Generate combined service report PDF |
| `pland service-report generate-pdf` | POST | Generate service report PDF |
| `pland service-report generate-zip` | POST | Generate service report ZIP archive |
| `pland service-report get` | GET | Get service report |
| `pland service-report get-count` | GET | Get service report count |
| `pland service-report get-last-number` | GET | Get last service report number |
| `pland service-report get-or-create-chat` | GET | Get or create service report chat |
| `pland service-report get-user` | GET | Get user service reports |
| `pland service-report list` | GET | List service reports |
| `pland service-report list-referenced-faktura-documents` | GET | List referenced faktura documents |
| `pland service-report set-fixed` | POST | Set service reports to fixed |
| `pland service-report set-multiple-to-faktured` | POST | Set multiple service reports to faktured |
| `pland service-report set-to-faktured` | POST | Set service report to faktured |
| `pland service-report set-to-finished` | POST | Set service reports to finished |
| `pland service-report sign` | POST | Sign service report |
| `pland service-report update` | PATCH | Update service report |

## signing

| Command | Methode | Beschreibung |
|---|---|---|
| `pland signing create` | POST | Create a new signing |
| `pland signing list-for-assignment` | GET | List signings for an assignment |
| `pland signing list-for-job` | GET | List signings for a job |

## sms

| Command | Methode | Beschreibung |
|---|---|---|
| `pland sms callback` | POST | SMS status callback |
| `pland sms track-clicked-link` | POST | Track clicked SMS link |

## suppliers

| Command | Methode | Beschreibung |
|---|---|---|
| `pland suppliers create` | POST | Create supplier |
| `pland suppliers delete` | DELETE | Delete supplier |
| `pland suppliers get` | GET | Get supplier |
| `pland suppliers get-last-number` | GET | Get last supplier number |
| `pland suppliers list` | GET | List suppliers |
| `pland suppliers update` | PATCH | Update supplier |

## surcharges

| Command | Methode | Beschreibung |
|---|---|---|
| `pland surcharges count` | GET | Count surcharges |
| `pland surcharges create` | POST | Create surcharge |
| `pland surcharges delete` | DELETE | Delete surcharge |
| `pland surcharges get` | GET | Get surcharge by ID |
| `pland surcharges get-distinct-values` | GET | Get distinct values |
| `pland surcharges list` | GET | List surcharges |
| `pland surcharges update` | PATCH | Update surcharge |
| `pland surcharges update-many` | PATCH | Batch update surcharges |

## task-types

| Command | Methode | Beschreibung |
|---|---|---|
| `pland task-types create` | POST | Create a new task type |
| `pland task-types delete` | DELETE | Deletes a task type |
| `pland task-types get` | GET | Get task type |
| `pland task-types list` | GET | List task types |
| `pland task-types update` | PATCH | Update task type |

## tasks

| Command | Methode | Beschreibung |
|---|---|---|
| `pland tasks complete` | POST | Complete task |
| `pland tasks create` | POST | Create task |
| `pland tasks delete-multiple` | POST | Delete multiple tasks |
| `pland tasks get` | GET | Get task |
| `pland tasks list` | GET | List tasks |
| `pland tasks resolve` | POST | Resolve task |
| `pland tasks update` | PATCH | Update task |

## tax-rates

| Command | Methode | Beschreibung |
|---|---|---|
| `pland tax-rates create` | POST | Create tax rate |
| `pland tax-rates delete` | DELETE | Delete tax rate |
| `pland tax-rates get` | GET | Get tax rate by ID |
| `pland tax-rates get-default` | GET | Get default tax rate |
| `pland tax-rates list` | GET | List tax rates |
| `pland tax-rates update` | PATCH | Update tax rate |

## time-tracking

| Command | Methode | Beschreibung |
|---|---|---|
| `pland time-tracking add-manually` | POST | Add time tracking manually (deprecated) |
| `pland time-tracking can-be-approved-by-target` | GET | Check if time tracking can be approved by target time |
| `pland time-tracking cancel` | POST | Cancel time tracking entry |
| `pland time-tracking filter` | GET | Filter time tracking entries |
| `pland time-tracking get-active` | GET | Get active time tracking status |
| `pland time-tracking get-not-approved-stamps` | GET | Get not approved time tracking entries |
| `pland time-tracking list-from-user` | GET | Get time tracking entries for a user |
| `pland time-tracking release-by-custom` | POST | Release time tracking with custom time (deprecated) |
| `pland time-tracking release-by-custom-by-admin` | POST | Release time tracking with custom time by admin (deprecated) |
| `pland time-tracking release-by-target` | POST | Release time tracking by target time (deprecated) |
| `pland time-tracking release-by-working` | POST | Release time tracking by working time (deprecated) |
| `pland time-tracking start-for-job` | POST | Start time tracking for a job |
| `pland time-tracking start-simple` | POST | Start simple time tracking |
| `pland time-tracking stop` | POST | Stop active time tracking |
| `pland time-tracking sync-offline` | POST | Sync single offline time tracking |
| `pland time-tracking sync-offline-batch` | POST | Sync multiple offline time tracking entries |
| `pland time-tracking un-cancel` | POST | Restore cancelled time tracking entry |

## upload

| Command | Methode | Beschreibung |
|---|---|---|
| `pland upload camt-transactions` | POST | camt v8 xml upload |
| `pland upload csv` | POST | CSV import for various entities |
| `pland upload get-image-safe` | GET | Get image by upload ID |
| `pland upload image` | POST | Image upload |
| `pland upload list` | GET | List all uploads |

## users

| Command | Methode | Beschreibung |
|---|---|---|
| `pland users count` | GET | Count users |
| `pland users create` | POST | Create a new user |
| `pland users delete` | DELETE | Delete user |
| `pland users filter` | POST | Filter users with advanced criteria |
| `pland users generate-password` | POST | Generate new password for user |
| `pland users get-all-employment-types` | GET | Get all employment types |
| `pland users get-available-tags` | GET | Get available user tags |
| `pland users get-by-id` | GET | Get user by ID |
| `pland users get-by-number` | GET | Get user by number |
| `pland users get-chat` | POST | Get or create user chat |
| `pland users get-distinct-values` | GET | Get user distinct values |
| `pland users get-last-number` | GET | Get last user number |
| `pland users list` | GET | List users |
| `pland users send-smsto-all` | POST | Send SMS credentials to all users |
| `pland users set-device-token` | POST | Set device token for push notifications |
| `pland users set-end-date-for-and-all-jobs` | POST | Set end date for user and their jobs |
| `pland users set-home-location` | POST | Set user home location |
| `pland users set-last-time-active` | POST | Update user last active time |
| `pland users set-profile-image` | POST | Set user profile image |
| `pland users set-web-push-token` | POST | Set web push token for browser notifications |
| `pland users update` | PATCH | Update user |
| `pland users update-many` | PATCH | Update multiple users |

## webhooks

| Command | Methode | Beschreibung |
|---|---|---|
| `pland webhooks create` | POST | Create a new webhook |
| `pland webhooks delete` | DELETE | Delete customer object |
| `pland webhooks list` | GET | List Webhooks |
| `pland webhooks update` | PATCH | Update Webhook |
