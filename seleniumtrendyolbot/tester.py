
sdata="""
   </div>

    <div class="ts-add-message ts-add-message-avatar-off" id="add-new-message" ng-class="{'ts-add-message-avatar-on': ctrl.userString,
                    'ts-add-message-avatar-off': !ctrl.isUserTyping,
                    'ts-add-smart-replies-on': (ctrl.deferRenderReady &amp;&amp; ctrl.viewModel.hasSmartReplies &amp;&amp; !ctrl.shouldHideSmartReplies),
                    'is-not-chat': !ctrl.isChat}" data-tid="channelNewMessageContainer">
      <!----><new-message ng-if="ctrl.isEditorInitialized || ctrl.showNewMessage || ctrl.shouldInitEditor" ng-show="ctrl.showNewMessage" is-composing-new-post="ctrl.isComposingNewPost" register-new-post-button-click-callback="ctrl.registerNewPostButtonClickedCallback(callback)" show-close-btn="ctrl.showCloseBtn" user-dismissed-compose="ctrl.userDismissedCompose" register-close-compose-callback="ctrl.registerCloseComposeCallback(callback)" class="chat-style" send-message="ctrl.sendMessageCallback(messageData, scenario)" on-up-arrow="ctrl.onUpArrow()" roster-size="ctrl.chatRosterSize" draft-conversation-item="ctrl.draftConversationItem" message-type="ctrl.messageType" is-new-chat="ctrl.isNewChat" conversation-id="ctrl.conversationId" block-attachments="ctrl.blockAttachments" show-subject="ctrl.showSubject" show-post-toolbar="ctrl.showPostToolbar" defer-load-ready="ctrl.deferNewMessageLoadReady" context="ctrl.context" pane-id="642f98d771d14fdbb7942bfd037f5b0e" show-meeting-create="ctrl.showMeetingCreate()" hide-people-picker="ctrl.hidePeoplePicker" do-not-focus-on-init="true" disable-compose="ctrl.disableCompose" disable-post-to-general="ctrl.disablePostToGeneral" is-team-archived="ctrl.isTeamArchived" register-disable-compose-callback="ctrl.registerDisableComposeCallback(callback)" register-focus-callback="ctrl.registerFocusCallback(callback)" register-draft-update-callback="ctrl.registerDraftUpdateCallback(callback)" register-recipient-chat-policy-update-callback="ctrl.registerRecipientChatPolicyUpdateCallback(callback)" update-roster-on-event="messageListRenderStateChanged" has-smart-replies="ctrl.viewModel.hasSmartReplies" should-hide-smart-replies="ctrl.shouldHideSmartReplies" smart-reply-options="ctrl.viewModel.smartReplyOptions" editor-initialized="ctrl.isEditorInitialized" show-banner-callback="ctrl.showNotificationBanner(key, args)" new-meetup="ctrl.newMeetup" should-hide-typing-indicator="ctrl.shouldHideTypingIndicator">
      <div class="ts-new-message ts-new-message-normal ts-border-newcompose  message-unimportant new-message-bg-light-f" ng-class="(isExpanded ? 'ts-new-message-expand' : 'ts-new-message-normal')  + ' ' +
               (!isReply ? 'ts-border-newcompose' : 'ts-border-reply') +
              ' ' + ' ' +
              (nmCtrl.messageIsHighImportance &amp;&amp; nmCtrl.isReplyConversation ? 'message-important' : 'message-unimportant') + ' ' +
              (currentUploads.length > 0 ? 'message-has-attachments' : '') + ' ' +
              (!nmCtrl.showCloseBtn &amp;&amp; nmCtrl.isFocused ? 'new-message-bg-light-f' : '')" ng-attr-id="{{rootIdentifier}}" data-tid="newMessage" simple-focusin="nmCtrl.onNewMessageFocus()" simple-focusout="nmCtrl.onNewMessageBlur()" simple-keydown="nmCtrl.onKeydown($event)" simple-keypress="nmCtrl.onKeypress($event)" id="ts-bottom-compose-identifier">
  <!---->
  <div class="new-message-banner new-message-common" ng-class="{ 'ts-new-message-isincorrectp2pchat' : nmCtrl.isDisabledP2PChatWithBanner }" title="">
    <notification-banner data-tid="newMessageNotificationBanner" notification-banner-store="nmCtrl.notificationBannerStore" skip-aria-live-update="true" tab="true" acc-role-dom="new-message-notification-banner"><div class="app-notification-banner tab-notification-banner" role="region" ng-class="[{ 'banner-show': banner }, { 'tab-notification-banner': tab }, bannerCss ]">
  <!---->
</div></notification-banner>
  </div>
  <!---->
  <!---->
  <div class="ts-new-message-footer new-message-common rich-style-enabled" data-tid="newMessageFooter" ng-show="!nmCtrl.newMeetup &amp;&amp; !nmCtrl.disableComposeBox &amp;&amp; !nmCtrl.isConversationWithBlockedBot &amp;&amp; !nmCtrl.isConversationWithOneWayBot &amp;&amp; !nmCtrl.disableNewMessageAndInputExtensions &amp;&amp; !nmCtrl.isConversationArchived" ng-class="{'ts-important': nmCtrl.messageIsHighImportance,
                  'ts-urgent': nmCtrl.messageIsUrgentImportance,
                  'ts-announcement-header': nmCtrl.enableComposePostToolbar &amp;&amp; nmCtrl.showPostToolbar &amp;&amp; nmCtrl.isAnnouncementLayout }">
    <files-dropzone on-drop="::nmCtrl.uploadDroppedFiles($files)" enable-zone="nmCtrl.enableDropUpload" track-scenario="::nmCtrl.dropScenario" track-module-name="::nmCtrl.dropModuleName"><!----><div class="files-dropzone" ng-if="$ctrl.enableZone" ngf-drop="" ngf-multiple="!$ctrl.disableMultiple" ngf-change="::$ctrl.droppedFilesCallback($files, $event)">
  <span ng-hide="::$ctrl.hideMessage" translate-once="files_dragCallToAction" class="">Dosyalarınızı buraya bırakın</span>
</div><!----></files-dropzone>
    <form novalidate="" class="ng-pristine ng-valid">
      <!----><div class="ts-new-message-pp" ng-if="!nmCtrl.hidePeoplePicker &amp;&amp; !nmCtrl.isInterop">
        <at-mentions id="pp_0f0a2fdc-1d79-4a6a-9400-21c3e0a4ca86" contact-selected="nmCtrl.addMention(contact, false, event)" search-results-updated="searchResultsChanged" search-text="searchText" hide-empty-results="hideEmptyResults" show-exact-matches-only="showExactMatchesOnly" search-filter="searchFilter" is-at-less-mention="isAtLessMention" team-id="" reply-chain-id="" conversation-id="19:a989da8113ef47cfbd17f1eb8b6d1e94@thread.v2" custom-class="" hide-logged-in-user="true" update-roster-on-event="messageListRenderStateChanged"><div class="ts-mentions" data-contactsavailable="true"><input sanitized="" id="pp_0f0a2fdc-1d79-4a6a-9400-21c3e0a4ca86_input" class="ts-search-input ng-pristine ng-untouched ng-valid ng-empty" ng-model="searchText" ng-keydown="keyDownHandler($event)" ng-keyup="keyUpHandler($event)" ng-blur="hideSearchResults()" ng-change="inputChanged(searchText)" focus-on="pp_0f0a2fdc-1d79-4a6a-9400-21c3e0a4ca86" placeholder="" autofocus=""><div class="ts-results"></div></div></at-mentions>
      </div><!---->
      <!----><input-extension-popover ng-if="nmCtrl.enableNewFullInputExtensions &amp;&amp; !nmCtrl.isInterop" command-text="inputExtensionSearchText" ctrlid="0f0a2fdc-1d79-4a6a-9400-21c3e0a4ca86" view-model="nmCtrl.inputExtensionCommandHandler.currentInputExtension">  <div class="ts-input-extension-popover">
    <div class="ts-results"></div>
  </div>
</input-extension-popover><!---->
      <!----><div ng-if="!nmCtrl.isInterop &amp;&amp; !nmCtrl.isLimitedChatExperience &amp;&amp; !nmCtrl.extendedSkypeEmoticons" class="ts-new-message-pp">
        <emoji-picker search-text="emojiSearchText"></emoji-picker>
      </div><!---->
      <!----><div class="bot-input-menu-container" ng-if="nmCtrl.enableBotInputMenu &amp;&amp; !nmCtrl.isInterop">
        <angucomplete-alt pause="0" search-str="" selected-object="executeBotInputMenuItem" search-fields="title" title-field="title" minlength="0" match-class="search-highlight" clear-selected="true" highlight-exact-match="false" hide-while-searching="true" hide-no-results="true" template-url="components/bot-input-menu/bot-input-menu.html">  <div stop-propagation="click" bot-input-menu-data="" key-handler-template="" event-type="botInputMenu" class="ts-bot-input-menu">
    <div class="ts-bot-input-menu-holder wide-mode">
      <div ng-show="showDropdown" class="dropup ng-hide">
        <ul id="_dropdown" class="ts-bot-input-menu-search-dropdown dropdown-menu angucomplete-dropdown" data-tid="ts-bot-input-menu-search-dropdown" acc-role-dom="menu" kb-list="" kb-cyclic="" role="menu">
          <!-- Load the floating menu -->
          <button class="ts-bot-input-menu-button ts-expand-button" ng-show="showFloatingMenu" ng-click="expandMenu($event);isHovered = false;" ng-class="{'ts-collapse-button': isExpanded, 'ts-expand-button': !isExpanded, 'hover': isHovered}" ng-mouseenter="isHovered = true" ng-mouseleave="isHovered = false" data-tid="ts-bot-input-menu-button" track-outcome="3" track-scenario="766" track-scenario-type="58" track-name="685" track-type="49" track-summary="Expand Input Menu">
            <span class="ts-bot-input-menu-button-text" translate-once="bot_inputMenu_floatingMenuLabel">Ne yapabilirim?</span>
            <!-- Load the chevron icon -->
            <!----><ng-include class="ts-bot-input-menu-chevron up" src="'svg/icons-triangle-up-small.html'"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-triangle-up-small"><polygon class="icons-default-fill" points="16,13 19.5,17 12.5,17"></polygon></svg></ng-include>
            <!----><ng-include class="ts-bot-input-menu-chevron down" src="'svg/icons-triangle-down-small.html'"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-triangle-down-small" focusable="false"><polygon class="icons-default-fill" points="16,19 19.5,15 12.5,15 "></polygon></svg></ng-include>
          </button>
          <!-- Show the suggestions label at the top while in dropdown search -->
          <div class="ts-bot-input-menu-label ng-hide" data-tid="ts-bot-input-menu-label" ng-show="!showFloatingMenu">
            <div class="ts-bot-input-menu-label-text" translate-once="bot_inputMenu_suggestionLabel">Öneriler</div>
          </div>
          <!---->
        </ul>
      </div>
    </div>
  </div>
</angucomplete-alt>
      </div><!---->
      <div class="ts-new-message-footer-content clearfix new-chicklet" ng-class="{'new-chicklet': nmCtrl.isNewChickletsEnabled,
                      'ts-expand-height': nmCtrl.enableComposePostToolbar &amp;&amp; nmCtrl.showPostToolbar,
                      'is-announcement': nmCtrl.isAnnouncementLayout}">
        <!---->
        <div data-tid="messageEditor" class="ts-message-editor ts-collapsed" ng-class="{'ts-expanded ts-expanded-half-height' : (nmCtrl.enableChannelNewPostButton || nmCtrl.msgChannelNewComposeTreatmentB) &amp;&amp; isExpanded,
                        'ts-expanded ts-expanded-full-height' : !nmCtrl.enableChannelNewPostButton &amp;&amp; !nmCtrl.msgChannelNewComposeTreatmentB &amp;&amp; isExpanded,
                        'ts-collapsed' : !isExpanded,
                        'ts-flex-container-subject' : isExpanded &amp;&amp; nmCtrl.showSubject,
                        'ts-post-toolbar' : nmCtrl.enableComposePostToolbar &amp;&amp; nmCtrl.showPostToolbar}" track-responsiveness="" track-responsiveness-source="composeMessage" track-responsiveness-event="keyup" tab-handler-context="" acc-role-dom="tab-handler-new-message-compose">
          <!---->
          <!---->
          <!----><div class="ts-message-icons" ng-class="{ 'ts-full-width' : isExpanded }" ng-if="!nmCtrl.isInterop &amp;&amp; !nmCtrl.isLimitedChatExperience">
            <!-- auto-close is not set to true because users need to be able to select text (outside of the popover)
              and then apply bold, italic, etc. (inside of the popover).-->
            <!--Shows 'A' formatting button if viewport is small-->
            <compose-format-toolbar format-command-source-id="new-message_78325826-0420-4114-bb28-9abe861bf6a4" disable-redbang="true" custom-container-acc-role="tab-handler-new-message-compose-icons" new-message-id="0f0a2fdc-1d79-4a6a-9400-21c3e0a4ca86" recalc-overflow="nmCtrl.recalcOverflow" enable-code-snippet="nmCtrl.enableCodeSnippet" toolbar-bounding-class="ts-message-editor"><div class="format-toolbar-container overflow-enabled" ng-class="::toolbarCtrl.overflowClass" role="menu" aria-label="Metni Biçimlendir" data-tid="textFormatButtons" ng-click="toolbarCtrl.catchToolbarClicks($event);" tabindex="-100" acc-role-dom="sub-menu tab-handler-new-message-compose-icons">
  <!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="textFormatBoldButton" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="Kalın, gezinmek için sol veya sağ ok tuşlarını kullanın ve etkinleştirmek için Enter tuşunu kullanın." title="Kalın (Ctrl+B)" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-bold app-icons-fill-focus inset-border-round " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem" id="textFormatBoldButton" track-outcome="4" track-scenario="101" track-scenario-type="36" track-name="86" track-type="23" track-summary="Bold">
      <!---->
      <!----><ng-include src="button.icon"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-bold"><g class="icons-default-fill"><path class="icons-unfilled" d="M11,23V9h5.1c1.6,0,2.8,0.3,3.6,0.9c0.8,0.6,1.3,1.4,1.3,2.4c0,0.8-0.3,1.4-0.8,2c-0.5,0.6-1.2,1-2,1.2v0
             c1,0.1,1.8,0.5,2.4,1.1c0.6,0.6,0.9,1.4,0.9,2.2c0,1.3-0.5,2.3-1.4,3.1C19.2,22.6,18,23,16.4,23H11z M14,11.3v3.3h1.4
             c0.7,0,1.2-0.2,1.5-0.5c0.4-0.3,0.6-0.8,0.6-1.3c0-1-0.8-1.5-2.3-1.5H14z M14,17v3.7h1.7c0.7,0,1.3-0.2,1.7-0.5
             c0.4-0.3,0.6-0.8,0.6-1.4c0-0.6-0.2-1-0.6-1.3c-0.4-0.3-1-0.5-1.7-0.5H14z"></path><path class="icons-filled" d="M16.4,23.5h-5.9v-15h5.6c1.7,0,3,0.3,3.9,1c1,0.7,1.5,1.7,1.5,2.8c0,0.8-0.3,1.6-0.9,2.3c-0.2,0.3-0.5,0.6-0.9,0.8
                   c0.5,0.2,0.9,0.5,1.2,0.9c0.7,0.7,1,1.6,1,2.6c0,1.4-0.5,2.5-1.6,3.5C19.4,23.1,18,23.5,16.4,23.5z M11.5,22.5h4.9
                   c1.4,0,2.5-0.3,3.4-1c0.8-0.7,1.2-1.6,1.2-2.7c0-0.7-0.3-1.4-0.8-1.8c-0.5-0.6-1.3-0.9-2.1-1l-2.9-0.3l2.8-0.7
                   c0.7-0.2,1.3-0.5,1.7-1c0.5-0.6,0.7-1.1,0.7-1.7c0-0.8-0.4-1.5-1.1-2c-0.7-0.5-1.8-0.8-3.3-0.8h-4.6V22.5z M15.7,21.2h-2.2v-4.7h2.2
                   c0.8,0,1.5,0.2,2,0.6c0.5,0.4,0.8,1,0.8,1.7c0,0.8-0.3,1.4-0.8,1.8C17.2,21,16.5,21.2,15.7,21.2z M14.5,20.2h1.2
                   c0.6,0,1.1-0.1,1.4-0.4c0.3-0.2,0.4-0.7,0.4-1c0-0.4-0.1-0.7-0.4-0.9c-0.3-0.3-0.9-0.4-1.4-0.4h-1.2V20.2z M15.4,15.1h-1.9v-4.3h1.7
                   c2.4,0,2.8,1.3,2.8,2c0,0.7-0.3,1.3-0.8,1.7C17,14.7,16.4,15.1,15.4,15.1z M14.5,14.1h0.9c0.5,0,0.9-0.1,1.1-0.4
                   c0.3-0.2,0.5-0.6,0.5-0.9c0-0.3,0-1-1.8-1h-0.7V14.1z
                   M16.4,23.5h-5.9v-15h5.6c1.7,0,3,0.3,3.9,1c1,0.7,1.5,1.7,1.5,2.8c0,0.8-0.3,1.6-0.9,2.3c-0.2,0.3-0.5,0.6-0.9,0.8
                   c0.5,0.2,0.9,0.5,1.2,0.9c0.7,0.7,1,1.6,1,2.6c0,1.4-0.5,2.5-1.6,3.5C19.4,23.1,18,23.5,16.4,23.5z M14.5,20.2h1.2
                   c0.6,0,1.1-0.1,1.4-0.4c0.3-0.2,0.4-0.7,0.4-1c0-0.4-0.1-0.7-0.4-0.9c-0.3-0.3-0.9-0.4-1.4-0.4h-1.2V20.2z M14.5,14.1h0.9
                   c0.5,0,0.9-0.1,1.1-0.4c0.3-0.2,0.5-0.6,0.5-0.9c0-0.3,0-1-1.8-1h-0.7V14.1z"></path></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="textFormatItalicButton" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="İtalik" title="İtalik (Ctrl+I)" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-italic app-icons-fill-focus inset-border-round " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem" track-outcome="4" track-scenario="102" track-scenario-type="36" track-name="87" track-type="23" track-summary="Italic">
      <!---->
      <!----><ng-include src="button.icon"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-italic"><g class="icons-default-fill"><path class="icons-unfilled" d="M22,9h-7c-0.2764,0-0.5,0.2236-0.5,0.5S14.7236,10,15,10h2.7456l-5.0769,12H10.5c-0.2764,0-0.5,0.2236-0.5,0.5
                   s0.2236,0.5,0.5,0.5h7c0.2764,0,0.5-0.2236,0.5-0.5S17.7764,22,17.5,22h-3.7456l5.0769-12H22c0.2764,0,0.5-0.2236,0.5-0.5
                   S22.2764,9,22,9z"></path><path class="icons-filled" d="M22,8.5h-7c-0.5522,0-1,0.4478-1,1s0.4478,1,1,1h1.9912l-4.6538,11H10.5c-0.5522,0-1,0.4478-1,1s0.4478,1,1,1h2.4947
                   c0.0016,0,0.0032,0.0005,0.0049,0.0005c0.0011,0,0.0022-0.0005,0.0033-0.0005H17.5c0.5522,0,1-0.4478,1-1s-0.4478-1-1-1h-2.9912
                   l4.6538-11H22c0.5522,0,1-0.4478,1-1S22.5522,8.5,22,8.5z"></path></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="textFormatUnderlineButton" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="Altı Çizili" title="Altı Çizili (Ctrl+U)" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-underline app-icons-fill-focus inset-border-round " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem" track-outcome="4" track-scenario="103" track-scenario-type="36" track-name="88" track-type="23" track-summary="Underline">
      <!---->
      <!----><ng-include src="button.icon"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-underline"><g class="icons-default-fill"><path class="icons-unfilled" d="M16,21c-2.7571,0-5-2.2432-5-5V9.5C11,9.2236,11.2239,9,11.5,9S12,9.2236,12,9.5V16c0,2.2056,1.7944,4,4,4s4-1.7944,4-4V9.5
                C20,9.2236,20.2239,9,20.5,9S21,9.2236,21,9.5V16C21,18.7568,18.7571,21,16,21z
                M20.5,24h-9c-0.2761,0-0.5-0.2236-0.5-0.5s0.2239-0.5,0.5-0.5h9c0.2761,0,0.5,0.2236,0.5,0.5S20.7761,24,20.5,24z"></path><path class="icons-filled" d="M16,21.5068c-3.0327,0-5.5-2.4673-5.5-5.5v-6.5c0-0.5522,0.4478-1,1-1s1,0.4478,1,1v6.5c0,1.9297,1.5701,3.5,3.5,3.5
                s3.5-1.5703,3.5-3.5v-6.5c0-0.5522,0.4478-1,1-1s1,0.4478,1,1v6.5C21.5,19.0396,19.0327,21.5068,16,21.5068z
                M20.5,23.9932h-9c-0.2761,0-0.5-0.2236-0.5-0.5s0.2239-0.5,0.5-0.5h9c0.2761,0,0.5,0.2236,0.5,0.5
                S20.7761,23.9932,20.5,23.9932z"></path></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="textFormatStrikeButton" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="Üstü çizili" title="Üstü çizili" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-strike app-icons-fill-focus inset-border-round " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem" id="textFormatStrikeButton" track-outcome="4" track-scenario="104" track-scenario-type="36" track-name="95" track-type="23" track-summary="Strikethrough">
      <!---->
      <!----><ng-include src="button.icon"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-redo"><g class="icons-default-fill"><path class="icons-unfilled" d="M24,16.5c0,0.2764-0.2236,0.5-0.5,0.5h-3.0587C20.7911,17.5166,21,18.1643,21,19c0,2.0938-2.4033,4-5.0415,4
          c-3.0713,0-4.769-1.959-4.8398-2.043c-0.1782-0.21-0.1523-0.5234,0.0571-0.7031c0.2095-0.1777,0.5254-0.1523,0.7041,0.0547
          C11.8945,20.3262,13.3657,22,15.9585,22C18.0361,22,20,20.542,20,19c0-0.8866-0.269-1.5254-0.9119-2H8.5C8.2236,17,8,16.7764,8,16.5
          S8.2236,16,8.5,16h7.4985h3.3682H23.5C23.7764,16,24,16.2236,24,16.5z
          M12.8402,15h3.244C12.002,14.3691,12,12.5555,12,11.9585
          C12,10.272,13.7197,9,16,9c2.6904,0,3.6104,1.4033,3.6533,1.4717c0.1445,0.2344,0.4482,0.3081,0.6846,0.168
          c0.2363-0.1426,0.3135-0.4497,0.1709-0.686C20.4609,9.8735,19.2969,8,16,8c-2.8506,0-5,1.7017-5,3.9585
          C11,13.2775,11.6235,14.2908,12.8402,15z"></path><path class="icons-filled" d="M24,16.5c0,0.2764-0.2236,0.5-0.5,0.5h-2.796c0.4816,0.6121,0.796,1.4178,0.796,2.5c0,2.3975-2.5898,4.5-5.5415,4.5
          c-3.2998,0-5.144-2.1289-5.2212-2.2188c-0.3569-0.4219-0.3052-1.0527,0.1157-1.4102c0.4224-0.3564,1.0522-0.3037,1.4097,0.1152
          C12.312,20.543,13.6128,22,15.9585,22c1.7876,0,3.5415-1.2383,3.5415-2.5c0-1.2626-0.5693-2.0372-3.5416-2.5H8.5
          C8.2236,17,8,16.7764,8,16.5S8.2236,16,8.5,16h4.2087h6.8252H23.5C23.7764,16,24,16.2236,24,16.5z M16.1288,15
          C12.5037,14.4307,12.5,12.9482,12.5,12.4585C12.5,11.0571,14.0049,10,16,10c2.3574,0,3.1797,1.1626,3.2314,1.2402
          c0.2891,0.4629,0.8936,0.6099,1.3643,0.3276c0.4727-0.2842,0.626-0.8989,0.3418-1.3721C20.8828,10.106,19.5762,8,16,8
          c-3.1357,0-5.5,1.9165-5.5,4.4585c0,0.8116,0.2208,1.7298,0.9363,2.5415H16.1288z"></path></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!---->
    <!----><span ng-if="::button.isSeparator" class="format-toolbar-separator-right" aria-hidden="true">
    </span><!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="textFormatHighlightButton" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="Metin vurgu rengi" title="Metin vurgu rengi" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-highlight app-icons-fill-focus inset-border-round " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem" data-prevent-refocus="true">
      <!---->
      <!----><ng-include src="button.icon"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-highlight"><g class="icons-default-fill"><path class="icons-unfilled" d="M23.5,9C23.2239,9,23,9.2236,23,9.5v2c0,0.2759-0.2244,0.5-0.5,0.5H20h-8H9.5C9.2244,12,9,11.7759,9,11.5v-2
                C9,9.2236,8.7761,9,8.5,9S8,9.2236,8,9.5v2C8,12.3271,8.6729,13,9.5,13H11v3.5c0,0.8271,0.6729,1.5,1.5,1.5H13v5.5
                c0,0.1802,0.0969,0.3462,0.2537,0.4351C13.3301,23.9785,13.415,24,13.5,24c0.0891,0,0.1782-0.0239,0.2573-0.0713l5-3
                C18.908,20.8384,19,20.6758,19,20.5V18h0.5c0.8271,0,1.5-0.6729,1.5-1.5V13h1.5c0.8271,0,1.5-0.6729,1.5-1.5v-2
                C24,9.2236,23.7761,9,23.5,9z M18,20.2168l-4,2.3999V18h4V20.2168z M20,16.5c0,0.2759-0.2244,0.5-0.5,0.5h-7
                c-0.2756,0-0.5-0.2241-0.5-0.5V13h8V16.5z"></path><path class="icons-filled" d="M23.5,9C23.2239,9,23,9.2236,23,9.5v2c0,0.2759-0.2244,0.5-0.5,0.5H20h-8H9.5C9.2244,12,9,11.7759,9,11.5v-2
                  C9,9.2236,8.7761,9,8.5,9S8,9.2236,8,9.5v2C8,12.3271,8.6729,13,9.5,13H11v3.5c0,0.8271,0.6729,1.5,1.5,1.5H13v5.5
                  c0,0.1802,0.0969,0.3462,0.2537,0.4351C13.3301,23.9785,13.415,24,13.5,24c0.0891,0,0.1782-0.0239,0.2573-0.0713l5-3
                  C18.908,20.8384,19,20.6758,19,20.5V18h0.5c0.8271,0,1.5-0.6729,1.5-1.5V13h1.5c0.8271,0,1.5-0.6729,1.5-1.5v-2
                  C24,9.2236,23.7761,9,23.5,9z M20,16.5c0,0.2759-0.2244,0.5-0.5,0.5h-7c-0.2756,0-0.5-0.2241-0.5-0.5V13h8V16.5z"></path></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="textFormatFontColorButton" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="Yazı tipi rengi" title="Yazı tipi rengi" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-font-color  app-icons-fill-focus inset-border-round " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem" data-prevent-refocus="true">
      <!---->
      <!----><ng-include src="button.icon"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-font-color"><g class="icons-default-fill"><path class="icons-unfilled" d="M20.5,23h-9c-0.2761,0-0.5,0.2236-0.5,0.5s0.2239,0.5,0.5,0.5h9c0.2761,0,0.5-0.2236,0.5-0.5S20.7761,23,20.5,23z
                M11.8357,20.9722c0.2617,0.0913,0.5459-0.0469,0.6365-0.3081L13.7467,17h4.5067l1.2745,3.6641
                C19.5996,20.8706,19.793,21,20,21c0.0544,0,0.1099-0.0088,0.1643-0.0278c0.2607-0.0908,0.3987-0.3755,0.3079-0.6362l-4-11.5
                C16.4023,8.6348,16.2129,8.5,16,8.5s-0.4023,0.1348-0.4722,0.3359l-4,11.5C11.437,20.5967,11.575,20.8813,11.8357,20.9722z
                M16,10.522L17.9055,16h-3.811L16,10.522z"></path><path class="icons-filled" d="M20.5,23h-9c-0.2761,0-0.5,0.2236-0.5,0.5s0.2239,0.5,0.5,0.5h9c0.2761,0,0.5-0.2236,0.5-0.5S20.7761,23,20.5,23z
          M11.6714,21.4443c0.5222,0.1831,1.0916-0.0942,1.2732-0.6157L14.1023,17.5h3.7953l1.1577,3.3286
          c0.1438,0.4126,0.5308,0.6719,0.9446,0.6719c0.1089,0,0.2197-0.0181,0.3286-0.0562c0.5215-0.1812,0.7974-0.7515,0.616-1.2729
          l-4-11.5C16.8047,8.2695,16.4255,8,16,8s-0.8047,0.2695-0.9446,0.6714l-4,11.5C10.874,20.6929,11.1499,21.2632,11.6714,21.4443z
          M16,12.0439L17.2021,15.5h-2.4041L16,12.0439z"></path></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="textFormatFontSizeButton" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="Yazı tipi boyutu" title="Yazı tipi boyutu" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-font-size app-icons-fill-focus inset-border-round " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem" data-prevent-refocus="true">
      <!---->
      <!----><ng-include src="button.icon"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-font-size"><g class="icons-default-fill"><path class="icons-unfilled" d="M22.9722,21.3357l-4-11.4999C18.9024,9.6348,18.713,9.5,18.5001,9.5s-0.4023,0.1348-0.4722,0.3357l-3.5177,10.1133
                l-2.0358-6.1073c-0.0681-0.2041-0.259-0.3418-0.4744-0.3418s-0.4062,0.1377-0.4744,0.3418l-2.5,7.4999
                c-0.0874,0.262,0.0542,0.5452,0.3162,0.6326c0.2624,0.0884,0.5454-0.0544,0.6326-0.3162l0.386-1.1582h3.2792l0.386,1.1582
                c0.0041,0.0122,0.0124,0.0214,0.0173,0.0331c0.0084,0.0201,0.0187,0.0378,0.0296,0.0566c0.0203,0.0349,0.0434,0.066,0.0706,0.0944
                c0.0137,0.0144,0.0266,0.0282,0.0421,0.041c0.0399,0.0327,0.0836,0.0586,0.1313,0.0776c0.0071,0.0028,0.0118,0.0087,0.0191,0.0113
                c0.0016,0.0005,0.0032,0.0001,0.0048,0.0007c0.051,0.0173,0.1045,0.0274,0.1595,0.0274c0.0057,0,0.0116-0.0026,0.0173-0.0028
                c0.0209-0.0007,0.04-0.0066,0.0605-0.0099c0.0269-0.0043,0.0537-0.0042,0.0804-0.0132c0.01-0.0033,0.0167-0.0112,0.0263-0.0151
                c0.0333-0.0134,0.0619-0.0324,0.0916-0.0526c0.0253-0.0172,0.0504-0.0328,0.0718-0.054c0.0219-0.0215,0.0381-0.0469,0.0558-0.0726
                c0.02-0.0289,0.039-0.0566,0.0526-0.089c0.0042-0.0099,0.0123-0.0166,0.0159-0.0269L16.2468,18h4.5065l1.2746,3.6643
                c0.0718,0.2063,0.2651,0.3359,0.4722,0.3359c0.0544,0,0.1099-0.009,0.1643-0.0281C22.9251,21.8815,23.063,21.5964,22.9722,21.3357z
                M10.6939,19.5l1.3063-3.9189L13.3064,19.5H10.6939z M16.5947,17l1.9054-5.478L20.4055,17H16.5947z"></path><path class="icons-filled" d="M23.4445,21.1713l-4-11.4999c-0.1399-0.4019-0.519-0.6714-0.9446-0.6714c-0.4255,0-0.8047,0.2695-0.9446,0.6714
                l-3.0353,8.7265l-1.5714-4.7141C12.8125,13.2754,12.4304,13,12,13c-0.4304,0-0.8125,0.2754-0.9487,0.6838l-2.5,7.4999
                c-0.1746,0.5239,0.1086,1.0901,0.6326,1.2649c0.5232,0.1746,1.0901-0.1082,1.2649-0.6326L10.7208,21h2.5584l0.2721,0.8162
                c0.0035,0.0105,0.011,0.0181,0.0148,0.0283c0.0331,0.0896,0.0749,0.1757,0.132,0.2526c0.0015,0.002,0.0031,0.0039,0.0046,0.006
                c0.0542,0.0718,0.1212,0.1334,0.1942,0.189c0.016,0.0121,0.0312,0.0242,0.0478,0.0353c0.0697,0.0468,0.1438,0.0884,0.2267,0.1173
                c0.0049,0.0017,0.0099,0.0019,0.0148,0.0035c0.0115,0.0038,0.0234,0.005,0.035,0.0084c0.082,0.024,0.1642,0.0359,0.2462,0.0387
                c0.0111,0.0004,0.0213,0.0051,0.0324,0.0051c0.0067,0,0.0135-0.0032,0.0202-0.0033c0.0956-0.0019,0.1886-0.0172,0.2782-0.0453
                c0.006-0.0019,0.0121-0.0009,0.018-0.0029c0.017-0.0057,0.0315-0.0151,0.048-0.0216c0.0366-0.0144,0.0724-0.0295,0.107-0.0481
                c0.0255-0.0136,0.0492-0.0289,0.0731-0.0445c0.0299-0.0195,0.059-0.0396,0.0868-0.0623c0.0232-0.019,0.0446-0.0393,0.0659-0.0601
                c0.0247-0.0241,0.0484-0.0487,0.0706-0.0755c0.0198-0.0239,0.0374-0.0489,0.0549-0.0744c0.0187-0.0274,0.0367-0.0548,0.0528-0.0844
                c0.0165-0.0302,0.03-0.0613,0.0433-0.093c0.0081-0.0192,0.0192-0.0363,0.0261-0.0562L16.6023,18.5h3.7953l1.1577,3.3286
                c0.1438,0.4128,0.5308,0.6716,0.9446,0.6716c0.1089,0,0.2197-0.0178,0.3286-0.0557C23.35,22.2629,23.6259,21.6931,23.4445,21.1713z
                M11.3875,19L12,17.1623L12.6125,19H11.3875z M17.2979,16.5l1.202-3.456l1.202,3.456H17.2979z"></path></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="textFormatRichStyleButton" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="Zengin stil" title="Zengin stil" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-rich-style  " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem" data-prevent-refocus="true">
      <!----><span ng-if="::button.label" class="rich-style-button-title">Paragraf</span><!---->
      <!----><ng-include src="button.icon"><svg viewBox="0 0 32 32" role="presentation" focusable="false" class="app-svg icons-dropdown"><g class="icons-default-fill"><path class="icons-unfilled" d="M16,21c-0.1,0-0.3,0-0.4-0.1l-7-7c-0.2-0.2-0.2-0.5,0-0.7s0.5-0.2,0.7,0l6.6,6.6l6.6-6.6c0.2-0.2,0.5-0.2,0.7,0 s0.2,0.5,0,0.7l-7,7C16.3,21,16.1,21,16,21z"></path><path class="icons-filled" d="M16,21.5c-0.256,0-0.512-0.098-0.707-0.293l-7-7c-0.391-0.39-0.391-1.024,0-1.414c0.391-0.391,1.023-0.391,1.414,0
                   L16,19.086l6.293-6.293c0.391-0.391,1.023-0.391,1.414,0c0.391,0.39,0.391,1.024,0,1.414l-7,7C16.512,21.402,16.256,21.5,16,21.5z"></path></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="textFormatRemoveFormatButton" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="Tüm biçimlendirmeyi temizle" title="Tüm biçimlendirmeyi temizle" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-removeformat app-icons-fill-focus inset-border-round " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem" id="textFormatRemoveFormatButton" track-outcome="4" track-scenario-type="36" track-name="96" track-type="23" track-summary="RemoveFormat">
      <!---->
      <!----><ng-include src="button.icon"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-redo"><g class="icons-default-fill"><path class="icons-unfilled" d="M23.8535,23.1465c0.1953,0.1953,0.1953,0.5117,0,0.707C23.7559,23.9512,23.6279,24,23.5,24s-0.2559-0.0488-0.3535-0.1465
          L21.5,22.207l-1.6465,1.6465C19.7559,23.9512,19.6279,24,19.5,24s-0.2559-0.0488-0.3535-0.1465
          c-0.1953-0.1953-0.1953-0.5117,0-0.707L20.793,21.5l-1.6465-1.6465c-0.1953-0.1953-0.1953-0.5117,0-0.707s0.5117-0.1953,0.707,0
          L21.5,20.793l1.6465-1.6465c0.1953-0.1953,0.5117-0.1953,0.707,0s0.1953,0.5117,0,0.707L22.207,21.5L23.8535,23.1465z
          M19.1875,11.3125c0.2266,0,0.4316-0.1543,0.4863-0.3843l0.3125-1.3125c0.0352-0.1489,0.001-0.3057-0.0938-0.4258S19.6533,9,19.5,9
          h-8c-0.2314,0-0.4326,0.1592-0.4863,0.3843l-0.3125,1.3125c-0.064,0.2686,0.1021,0.5381,0.3706,0.6021
          c0.2686,0.0649,0.5381-0.1011,0.6021-0.3706L11.895,10h2.9951l-1.7999,9H12c-0.2764,0-0.5,0.2236-0.5,0.5S11.7236,20,12,20h3
          c0.2764,0,0.5-0.2236,0.5-0.5S15.2764,19,15,19h-0.8903l1.8001-9h2.9573l-0.166,0.6968c-0.0645,0.2686,0.1016,0.5381,0.3701,0.6021
          C19.1104,11.3081,19.1494,11.3125,19.1875,11.3125z M17.5,22h-8C9.2236,22,9,22.2236,9,22.5S9.2236,23,9.5,23h8
          c0.2764,0,0.5-0.2236,0.5-0.5S17.7764,22,17.5,22z"></path><path class="icons-filled" d="M23.8535,23.1465c0.1953,0.1953,0.1953,0.5117,0,0.707C23.7559,23.9512,23.6279,24,23.5,24s-0.2559-0.0488-0.3535-0.1465
          L21.5,22.207l-1.6465,1.6465C19.7559,23.9512,19.6279,24,19.5,24s-0.2559-0.0488-0.3535-0.1465
          c-0.1953-0.1953-0.1953-0.5117,0-0.707L20.793,21.5l-1.6465-1.6465c-0.1953-0.1953-0.1953-0.5117,0-0.707s0.5117-0.1953,0.707,0
          L21.5,20.793l1.6465-1.6465c0.1953-0.1953,0.5117-0.1953,0.707,0s0.1953,0.5117,0,0.707L22.207,21.5L23.8535,23.1465z
          M20.1602,10.5439l0.3125-1.3125c0.0713-0.2974,0.002-0.6113-0.1875-0.8511C20.0947,8.1401,19.8057,8,19.5,8h-8
          c-0.4629,0-0.8657,0.3179-0.9727,0.7686l-0.3125,1.3125c-0.1279,0.5371,0.2036,1.0762,0.7412,1.2041s1.0762-0.2036,1.2041-0.7412
          L12.29,10h1.9902l-1.6,8H12c-0.5522,0-1,0.4473-1,1s0.4478,1,1,1h3c0.5522,0,1-0.4473,1-1s-0.4478-1-1-1h-0.2803l1.6-8h1.9147
          l-0.0195,0.0811c-0.1279,0.5371,0.2041,1.0762,0.7412,1.2041c0.0781,0.0186,0.1553,0.0273,0.2324,0.0273
          C19.6406,11.3125,20.0508,11.0034,20.1602,10.5439z M17.5,22h-8C9.2236,22,9,22.2236,9,22.5S9.2236,23,9.5,23h8
          c0.2764,0,0.5-0.2236,0.5-0.5S17.7764,22,17.5,22z"></path></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!---->
    <!----><span ng-if="::button.isSeparator" class="format-toolbar-separator-right" aria-hidden="true">
    </span><!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="textFormatOutdentButton" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="Girintiyi azalt" title="Girintiyi azalt" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-outdent app-icons-fill-focus inset-border-round " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem" id="textFormatOutdentButton" track-outcome="4" track-scenario-type="36" track-name="98" track-type="23" track-summary="Outdent">
      <!---->
      <!----><ng-include src="button.icon"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-outdent"><g class="icons-default-fill"><path class="icons-unfilled" d="M20.8438,11.1484c0.0986,0.0991,0.1484,0.2163,0.1484,0.3516c0,0.1357-0.0498,0.2529-0.1484,0.3516
          C20.7451,11.9507,20.6279,12,20.4922,12h-7c-0.1357,0-0.2529-0.0493-0.3516-0.1484c-0.0986-0.0986-0.1484-0.2158-0.1484-0.3516
          c0-0.1353,0.0498-0.2524,0.1484-0.3516C13.2393,11.0498,13.3564,11,13.4922,11h7C20.6279,11,20.7451,11.0498,20.8438,11.1484z
          M23.8438,16.1484c0.0986,0.0991,0.1484,0.2163,0.1484,0.3516c0,0.1357-0.0498,0.2529-0.1484,0.3516
          C23.7451,16.9507,23.6279,17,23.4922,17h-10c-0.1357,0-0.2529-0.0493-0.3516-0.1484c-0.0986-0.0986-0.1484-0.2158-0.1484-0.3516
          c0-0.1353,0.0498-0.2524,0.1484-0.3516C13.2393,16.0498,13.3564,16,13.4922,16h10C23.6279,16,23.7451,16.0498,23.8438,16.1484z
          M19.8438,21.1484c0.0986,0.0986,0.1484,0.2158,0.1484,0.3516s-0.0498,0.2529-0.1484,0.3516S19.6279,22,19.4922,22h-6
          c-0.1357,0-0.2529-0.0498-0.3516-0.1484s-0.1484-0.2158-0.1484-0.3516s0.0498-0.2529,0.1484-0.3516S13.3564,21,13.4922,21h6
          C19.6279,21,19.7451,21.0498,19.8438,21.1484z
          M10.8535,18.8535c0.1953-0.1953,0.1953-0.5117,0-0.707L9.207,16.5l1.6465-1.6465
          c0.1953-0.1953,0.1953-0.5117,0-0.707s-0.5117-0.1953-0.707,0l-2,2c-0.1953,0.1953-0.1953,0.5117,0,0.707l2,2
          C10.2441,18.9512,10.3721,19,10.5,19S10.7559,18.9512,10.8535,18.8535z"></path><path class="icons-filled" d="M10.5,19c-0.1279,0-0.2559-0.0488-0.3535-0.1465l-2-2c-0.1953-0.1953-0.1953-0.5117,0-0.707l2-2
          c0.1953-0.1953,0.5117-0.1953,0.707,0s0.1953,0.5117,0,0.707L9.207,16.5l1.6465,1.6465c0.1953,0.1953,0.1953,0.5117,0,0.707
          C10.7559,18.9512,10.6279,19,10.5,19z M21,11c0-0.5522-0.4473-1-1-1h-6c-0.5522,0-1,0.4478-1,1s0.4478,1,1,1h6
          C20.5527,12,21,11.5522,21,11z
          M24,16c0-0.5522-0.4473-1-1-1h-9c-0.5522,0-1,0.4478-1,1s0.4478,1,1,1h9C23.5527,17,24,16.5522,24,16
          z M20,21c0-0.5527-0.4473-1-1-1h-5c-0.5522,0-1,0.4473-1,1s0.4478,1,1,1h5C19.5527,22,20,21.5527,20,21z"></path></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="textFormatIndentButton" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="Girintiyi artır" title="Girintiyi artır" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-indent app-icons-fill-focus inset-border-round " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem" id="textFormatIndentButton" track-outcome="4" track-scenario-type="36" track-name="97" track-type="23" track-summary="Indent">
      <!---->
      <!----><ng-include src="button.icon"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-indent"><g class="icons-default-fill"><path class="icons-unfilled" d="M20.8438,11.1484c0.0986,0.0991,0.1484,0.2163,0.1484,0.3516c0,0.1357-0.0498,0.2529-0.1484,0.3516
          C20.7451,11.9507,20.6279,12,20.4922,12h-7c-0.1357,0-0.2529-0.0493-0.3516-0.1484c-0.0986-0.0986-0.1484-0.2158-0.1484-0.3516
          c0-0.1353,0.0498-0.2524,0.1484-0.3516C13.2393,11.0498,13.3564,11,13.4922,11h7C20.6279,11,20.7451,11.0498,20.8438,11.1484z
          M23.8438,16.1484c0.0986,0.0991,0.1484,0.2163,0.1484,0.3516c0,0.1357-0.0498,0.2529-0.1484,0.3516
          C23.7451,16.9507,23.6279,17,23.4922,17h-10c-0.1357,0-0.2529-0.0493-0.3516-0.1484c-0.0986-0.0986-0.1484-0.2158-0.1484-0.3516
          c0-0.1353,0.0498-0.2524,0.1484-0.3516C13.2393,16.0498,13.3564,16,13.4922,16h10C23.6279,16,23.7451,16.0498,23.8438,16.1484z
          M19.8438,21.1484c0.0986,0.0986,0.1484,0.2158,0.1484,0.3516s-0.0498,0.2529-0.1484,0.3516S19.6279,22,19.4922,22h-6
          c-0.1357,0-0.2529-0.0498-0.3516-0.1484s-0.1484-0.2158-0.1484-0.3516s0.0498-0.2529,0.1484-0.3516S13.3564,21,13.4922,21h6
          C19.6279,21,19.7451,21.0498,19.8438,21.1484z M8.8535,18.8535l2-2c0.1953-0.1953,0.1953-0.5117,0-0.707l-2-2
          c-0.1953-0.1953-0.5117-0.1953-0.707,0s-0.1953,0.5117,0,0.707L9.793,16.5l-1.6465,1.6465c-0.1953,0.1953-0.1953,0.5117,0,0.707
          C8.2441,18.9512,8.3721,19,8.5,19S8.7559,18.9512,8.8535,18.8535z"></path><path class="icons-filled" d="M8.5,19c-0.1279,0-0.2559-0.0488-0.3535-0.1465c-0.1953-0.1953-0.1953-0.5117,0-0.707L9.793,16.5l-1.6465-1.6465
          c-0.1953-0.1953-0.1953-0.5117,0-0.707s0.5117-0.1953,0.707,0l2,2c0.1953,0.1953,0.1953,0.5117,0,0.707l-2,2
          C8.7559,18.9512,8.6279,19,8.5,19z M21,11c0-0.5522-0.4473-1-1-1h-6c-0.5522,0-1,0.4478-1,1s0.4478,1,1,1h6
          C20.5527,12,21,11.5522,21,11z
          M24,16c0-0.5522-0.4473-1-1-1h-9c-0.5522,0-1,0.4478-1,1s0.4478,1,1,1h9C23.5527,17,24,16.5522,24,16
          z M20,21c0-0.5527-0.4473-1-1-1h-5c-0.5522,0-1,0.4473-1,1s0.4478,1,1,1h5C19.5527,22,20,21.5527,20,21z"></path></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="textFormatBulletsButton" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="Madde işaretli liste" title="Madde işaretli liste" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-bullets app-icons-fill-focus inset-border-round " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem" track-outcome="4" track-scenario="112" track-scenario-type="36" track-name="116" track-type="23" track-summary="Bullet">
      <!---->
      <!----><ng-include src="button.icon"><svg viewBox="0 0 32 32" role="presentation" focusable="false" class="app-svg icons-bullets"><g class="icons-default-fill"><g class="icons-unfilled"><path d="M13.5 11h9a.5.5 0 0 0 0-1h-9a.5.5 0 0 0 0 1zM22.5 15h-9a.5.5 0 0 0 0 1h9a.5.5 0 0 0 0-1zM22.5 20h-9a.5.5 0 0 0 0 1h9a.5.5 0 0 0 0-1z"></path><circle cx="10.5" cy="10.5" r="1"></circle><circle cx="10.5" cy="20.5" r="1"></circle><circle cx="10.5" cy="15.5" r="1"></circle></g><g class="icons-filled"><circle cx="10.5" cy="10.5" r="1"></circle><circle cx="10.5" cy="20.5" r="1"></circle><circle cx="10.5" cy="15.5" r="1"></circle><path d="M13.5 11.25h9a.75.75 0 0 0 0-1.5h-9a.75.75 0 0 0 0 1.5zm9 3.5h-9a.75.75 0 0 0 0 1.5h9a.75.75 0 0 0 0-1.5zm0 5h-9a.75.75 0 0 0 0 1.5h9a.75.75 0 0 0 0-1.5z"></path></g></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="textFormatNumbersButton" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="Numaralı liste" title="Numaralı liste" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-number-list app-icons-fill-focus inset-border-round " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem" track-outcome="4" track-scenario="113" track-scenario-type="36" track-name="117" track-type="23" track-summary="List">
      <!---->
      <!----><ng-include src="button.icon"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-number-list"><g class="icons-default-fill"><path class="icons-unfilled" d="M13.5,11h9c0.2761,0,0.5-0.2236,0.5-0.5S22.7761,10,22.5,10h-9c-0.2761,0-0.5,0.2236-0.5,0.5S13.2239,11,13.5,11z
             M22.5,15h-9c-0.2761,0-0.5,0.2236-0.5,0.5s0.2239,0.5,0.5,0.5h9c0.2761,0,0.5-0.2236,0.5-0.5S22.7761,15,22.5,15z
             M22.5,20h-9c-0.2761,0-0.5,0.2236-0.5,0.5s0.2239,0.5,0.5,0.5h9c0.2761,0,0.5-0.2236,0.5-0.5S22.7761,20,22.5,20z
             M11.1783,14.3018c-0.1046-0.0968-0.2323-0.1716-0.3832-0.2235C10.6444,14.0259,10.4739,14,10.284,14
                   c-0.4096,0-0.7776,0.1107-1.1035,0.3317v0.7632c0.2946-0.2693,0.6031-0.4035,0.9257-0.4035c0.1866,0,0.3252,0.0429,0.4158,0.1292
                   c0.0906,0.0858,0.136,0.213,0.136,0.3811c0,0.0858-0.014,0.1671-0.0418,0.2429c-0.0278,0.0758-0.0701,0.1507-0.1267,0.225
                   c-0.0568,0.0738-0.1265,0.1487-0.2092,0.2235c-0.083,0.0748-0.1793,0.1536-0.2891,0.2359
                   c-0.1046,0.0788-0.2149,0.1671-0.3309,0.2649c-0.1158,0.0978-0.2225,0.21-0.3202,0.3372s-0.1788,0.2708-0.2432,0.431
                   S9,17.5027,9,17.7037V18h2.4948v-0.7188h-1.59c0-0.0514,0.0174-0.1052,0.0523-0.1621c0.0349-0.0564,0.082-0.1147,0.1412-0.1741
                   s0.1277-0.1197,0.2052-0.1811c0.0777-0.0613,0.1583-0.1227,0.242-0.1851c0.1239-0.0898,0.2432-0.1826,0.3583-0.2783
                   c0.1151-0.0963,0.2166-0.202,0.3045-0.3167c0.0882-0.1158,0.1588-0.2434,0.2121-0.3841c0.053-0.1412,0.0796-0.3023,0.0796-0.4828
                   c0-0.1706-0.0273-0.3242-0.0825-0.4624C11.3628,14.5163,11.283,14.3986,11.1783,14.3018z
             M9.5419,10.1911c0.0859-0.0302,0.1672-0.064,0.2434-0.1012C9.8619,10.0527,9.944,10.013,10,9.9713V13h1V9h-0.6161
                   c-0.1891,0.122-0.4012,0.2336-0.6355,0.3358C9.5141,9.4376,9.2645,9.5214,9,9.5869v0.7253
                   c0.0903-0.0089,0.1818-0.0238,0.2742-0.0446S9.456,10.2209,9.5419,10.1911z
             M10.6028,20.9228v-0.0132c0.5197-0.1275,0.7795-0.4443,0.7795-0.9494c0-0.2839-0.1116-0.5154-0.3352-0.6929
                   C10.8239,19.0887,10.5116,19,10.1105,19c-0.3665,0-0.6875,0.0681-0.9628,0.205v0.6959c0.2479-0.1672,0.5033-0.2511,0.7659-0.2511
                   c0.3921,0,0.5881,0.1574,0.5881,0.4722c0,0.3344-0.2554,0.5016-0.7659,0.5016H9.3994v0.6527h0.3638
                   c0.2663,0,0.4754,0.0466,0.6276,0.1403c0.1524,0.0937,0.2285,0.2266,0.2285,0.3992c0,0.1672-0.0614,0.2977-0.1848,0.3908
                   c-0.1228,0.0937-0.2949,0.1403-0.5155,0.1403c-0.3501,0-0.6564-0.0941-0.919-0.283v0.7419C9.2534,22.9353,9.5826,23,9.9874,23
                   c0.4722,0,0.8424-0.1055,1.1105-0.3158c0.268-0.2104,0.4021-0.4963,0.4021-0.8577c0-0.2393-0.0803-0.4409-0.2407-0.6056
                   C11.0989,21.0566,10.8801,20.9571,10.6028,20.9228z"></path><path class="icons-filled" d="M13.5,11.25h9c0.4143,0,0.75-0.3359,0.75-0.75s-0.3357-0.75-0.75-0.75h-9c-0.4143,0-0.75,0.3359-0.75,0.75
                   S13.0857,11.25,13.5,11.25z
             M22.5,14.75h-9c-0.4143,0-0.75,0.3359-0.75,0.75s0.3357,0.75,0.75,0.75h9c0.4143,0,0.75-0.3359,0.75-0.75
                   S22.9143,14.75,22.5,14.75z
             M22.5,19.75h-9c-0.4143,0-0.75,0.3359-0.75,0.75s0.3357,0.75,0.75,0.75h9c0.4143,0,0.75-0.3359,0.75-0.75
                   S22.9143,19.75,22.5,19.75z
             M11.1783,14.3018c-0.1046-0.0968-0.2323-0.1716-0.3832-0.2235C10.6444,14.0259,10.4739,14,10.284,14
                   c-0.4096,0-0.7776,0.1107-1.1035,0.3317v0.7632c0.2946-0.2693,0.6031-0.4035,0.9257-0.4035c0.1866,0,0.3252,0.0429,0.4158,0.1292
                   c0.0906,0.0858,0.136,0.213,0.136,0.3811c0,0.0858-0.014,0.1671-0.0418,0.2429c-0.0278,0.0758-0.0701,0.1507-0.1267,0.225
                   c-0.0568,0.0738-0.1265,0.1487-0.2092,0.2235c-0.083,0.0748-0.1793,0.1536-0.2891,0.2359
                   c-0.1046,0.0788-0.2149,0.1671-0.3309,0.2649c-0.1158,0.0978-0.2225,0.21-0.3202,0.3372s-0.1788,0.2708-0.2432,0.431
                   S9,17.5027,9,17.7037V18h2.4948v-0.7188h-1.59c0-0.0514,0.0174-0.1052,0.0523-0.1621c0.0349-0.0564,0.082-0.1147,0.1412-0.1741
                   s0.1277-0.1197,0.2052-0.1811c0.0777-0.0613,0.1583-0.1227,0.242-0.1851c0.1239-0.0898,0.2432-0.1826,0.3583-0.2783
                   c0.1151-0.0963,0.2166-0.202,0.3045-0.3167c0.0882-0.1158,0.1588-0.2434,0.2121-0.3841c0.053-0.1412,0.0796-0.3023,0.0796-0.4828
                   c0-0.1706-0.0273-0.3242-0.0825-0.4624C11.3628,14.5163,11.283,14.3986,11.1783,14.3018z
             M9.5419,10.1911c0.0859-0.0302,0.1672-0.064,0.2434-0.1012C9.8619,10.0527,9.944,10.013,10,9.9713V13h1V9h-0.6161
                   c-0.1891,0.122-0.4012,0.2336-0.6355,0.3358C9.5141,9.4376,9.2645,9.5214,9,9.5869v0.7253
                   c0.0903-0.0089,0.1818-0.0238,0.2742-0.0446S9.456,10.2209,9.5419,10.1911z
             M10.6028,20.9228v-0.0132c0.5197-0.1275,0.7795-0.4443,0.7795-0.9494c0-0.2839-0.1116-0.5154-0.3352-0.6929
                   C10.8239,19.0887,10.5116,19,10.1105,19c-0.3665,0-0.6875,0.0681-0.9628,0.205v0.6959c0.2479-0.1672,0.5033-0.2511,0.7659-0.2511
                   c0.3921,0,0.5881,0.1574,0.5881,0.4722c0,0.3344-0.2554,0.5016-0.7659,0.5016H9.3994v0.6527h0.3638
                   c0.2663,0,0.4754,0.0466,0.6276,0.1403c0.1524,0.0937,0.2285,0.2266,0.2285,0.3992c0,0.1672-0.0614,0.2977-0.1848,0.3908
                   c-0.1228,0.0937-0.2949,0.1403-0.5155,0.1403c-0.3501,0-0.6564-0.0941-0.919-0.283v0.7419C9.2534,22.9353,9.5826,23,9.9874,23
                   c0.4722,0,0.8424-0.1055,1.1105-0.3158c0.268-0.2104,0.4021-0.4963,0.4021-0.8577c0-0.2393-0.0803-0.4409-0.2407-0.6056
                   C11.0989,21.0566,10.8801,20.9571,10.6028,20.9228z"></path></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!---->
    <!----><span ng-if="::button.isSeparator" class="format-toolbar-separator-right" aria-hidden="true">
    </span><!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="textFormatBlockQuoteButton" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="Alıntı" title="Alıntı" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-quote app-icons-fill-focus inset-border-round " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem">
      <!---->
      <!----><ng-include src="button.icon"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-quote"><g class="icons-default-fill"><g class="icons-filled"><path d="M12,11.5c-1.37842,0-2.5,1.12158-2.5,2.5s1.12158,2.5,2.5,2.5c0.11328,0,0.22607-0.00781,0.3374-0.02393c-0.22266,1.26318-0.7168,2.2876-1.61377,3.39307c-0.34668,0.42773-0.28174,1.05859,0.14648,1.4082C11.04736,21.4209,11.271,21.5,11.49951,21.5c0.30225,0,0.58545-0.13477,0.77686-0.36914C14.32812,18.60156,14.5,16.41699,14.5,14.396C14.5,12.39551,13.24414,11.5,12,11.5z"></path><path d="M20,11.5c-1.37891,0-2.5,1.12158-2.5,2.5s1.12109,2.5,2.5,2.5c0.11328,0,0.22559-0.00781,0.33691-0.02393c-0.22266,1.26416-0.7168,2.28857-1.61426,3.39404c-0.3457,0.42773-0.28027,1.05859,0.14648,1.40527C19.0459,21.41992,19.26953,21.5,19.5,21.5c0.30078,0,0.58301-0.13379,0.77734-0.36914C22.32812,18.60156,22.5,16.41699,22.5,14.396C22.5,12.39551,21.24414,11.5,20,11.5z"></path></g><g class="icons-unfilled"><path d="M12,12c-1.10455,0-2,0.89539-2,2c0,1.10455,0.89545,2,2,2c0.3399,0,0.65509-0.09271,0.93536-0.24231c-0.13416,1.49384-0.54962,2.85699-1.82355,4.42688c-0.17432,0.21484-0.14111,0.5293,0.07324,0.7041C11.27783,20.96387,11.38916,21,11.49951,21c0.14551,0,0.29004-0.06348,0.38867-0.18457C13.84473,18.4043,14,16.3125,14,14.39583C14,12.79167,13.10455,12,12,12z"></path><path d="M20,12c-1.10455,0-2,0.89539-2,2c0,1.10455,0.89545,2,2,2c0.3399,0,0.65509-0.09271,0.93536-0.24231c-0.13416,1.49384-0.54962,2.85699-1.82355,4.42688c-0.17432,0.21484-0.14111,0.5293,0.07324,0.7041C19.27783,20.96387,19.38916,21,19.49951,21c0.14551,0,0.29004-0.06348,0.38867-0.18457C21.84473,18.4043,22,16.3125,22,14.39583C22,12.79167,21.10455,12,20,12z"></path></g></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="textFormatInsertHyperlinkButton" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="Bağlantı ekleyin" title="Bağlantı ekleyin" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-link app-icons-fill-focus inset-border-round " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem" track-outcome="4" track-scenario="146" track-scenario-type="36" track-name="147" track-type="23" track-summary="Add or edit hyperlink" data-prevent-refocus="true">
      <!---->
      <!----><ng-include src="button.icon"><svg viewBox="-6 -6 32 32" focusable="false" role="presentation" class="app-svg icons-link icons-fluent"><g class="icons-default-fill"><path class="icons-unfilled" d="M8 6C8.27614 6 8.5 6.22386 8.5 6.5C8.5 6.74546 8.32312 6.94961 8.08988 6.99194L8 7H6C4.34315 7 3 8.34315 3 10C3 11.5906 4.23784 12.892 5.80275 12.9936L6 13H8C8.27614 13 8.5 13.2239 8.5 13.5C8.5 13.7455 8.32312 13.9496 8.08988 13.9919L8 14H6C3.79086 14 2 12.2091 2 10C2 7.8645 3.67346 6.11986 5.78053 6.00592L6 6H8ZM14 6C16.2091 6 18 7.79086 18 10C18 12.1355 16.3265 13.8801 14.2195 13.9941L14 14H12C11.7239 14 11.5 13.7761 11.5 13.5C11.5 13.2545 11.6769 13.0504 11.9101 13.0081L12 13H14C15.6569 13 17 11.6569 17 10C17 8.40942 15.7622 7.10795 14.1973 7.00638L14 7H12C11.7239 7 11.5 6.77614 11.5 6.5C11.5 6.25454 11.6769 6.05039 11.9101 6.00806L12 6H14ZM6 9.5H14C14.2761 9.5 14.5 9.72386 14.5 10C14.5 10.2455 14.3231 10.4496 14.0899 10.4919L14 10.5H6C5.72386 10.5 5.5 10.2761 5.5 10C5.5 9.75454 5.67688 9.55039 5.91012 9.50806L6 9.5H14H6Z"></path><path class="icons-filled" d="M14 6C16.2091 6 18 7.79086 18 10C18 12.1422 16.316 13.8911 14.1996 13.9951L14 14H12C11.5858 14 11.25 13.6642 11.25 13.25C11.25 12.8703 11.5322 12.5565 11.8982 12.5068L12 12.5H14C15.3807 12.5 16.5 11.3807 16.5 10C16.5 8.67452 15.4685 7.58996 14.1644 7.50532L14 7.5H12C11.5858 7.5 11.25 7.16421 11.25 6.75C11.25 6.3703 11.5322 6.05651 11.8982 6.00685L12 6H14ZM8 6C8.41421 6 8.75 6.33579 8.75 6.75C8.75 7.1297 8.46785 7.44349 8.10177 7.49315L8 7.5H6C4.61929 7.5 3.5 8.61929 3.5 10C3.5 11.3255 4.53154 12.41 5.83562 12.4947L6 12.5H8C8.41421 12.5 8.75 12.8358 8.75 13.25C8.75 13.6297 8.46785 13.9435 8.10177 13.9932L8 14H6C3.79086 14 2 12.2091 2 10C2 7.8578 3.68397 6.10892 5.80036 6.0049L6 6H8ZM6.25 9.25H13.75C14.1642 9.25 14.5 9.58579 14.5 10C14.5 10.3797 14.2178 10.6935 13.8518 10.7432L13.75 10.75H6.25C5.83579 10.75 5.5 10.4142 5.5 10C5.5 9.6203 5.78215 9.30651 6.14823 9.25685L6.25 9.25H13.75H6.25Z"></path></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="insertCodeSnippetButton" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="Kod parçacığı" title="Kod parçacığı" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-codesnippet app-icons-fill-focus inset-border-round " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem" track-outcome="8" track-scenario="92" track-scenario-type="36" track-name="71" track-type="23" track-summary="Show code snippet dialog">
      <!---->
      <!----><ng-include src="button.icon"><svg role="presentation" class="app-svg icons-codesnippet" viewBox="0 0 32 32" focusable="false"><g class="icons-default-fill"><g class="icons-unfilled"><path d="M20,20c-0.115,0-0.231-0.039-0.325-0.12c-0.21-0.18-0.234-0.496-0.055-0.705L22.342,16l-2.722-3.175c-0.18-0.209-0.155-0.525,0.055-0.705c0.209-0.179,0.524-0.156,0.705,0.054l3,3.5c0.16,0.187,0.16,0.463,0,0.65l-3,3.5C20.28,19.94,20.141,20,20,20z"></path><path d="M14.251,23.5c-0.046,0-0.092-0.006-0.138-0.02c-0.266-0.075-0.419-0.353-0.344-0.618l4-14c0.075-0.266,0.349-0.419,0.618-0.344c0.266,0.076,0.419,0.353,0.343,0.618l-4,14C14.668,23.357,14.468,23.5,14.251,23.5z"></path><path d="M12,20c0.115,0,0.231-0.039,0.325-0.12c0.21-0.18,0.234-0.496,0.055-0.705L9.658,16l2.722-3.175c0.18-0.209,0.155-0.525-0.055-0.705c-0.209-0.179-0.524-0.156-0.705,0.054l-3,3.5c-0.16,0.187-0.16,0.463,0,0.65l3,3.5C11.72,19.94,11.859,20,12,20z"></path></g><g class="icons-filled"><path d="M20,20.5c-0.23,0-0.462-0.079-0.65-0.241c-0.42-0.359-0.469-0.99-0.108-1.409L21.683,16l-2.441-2.849c-0.36-0.419-0.312-1.051,0.108-1.41c0.419-0.359,1.051-0.311,1.409,0.108l3,3.5c0.321,0.375,0.321,0.927,0,1.301l-3,3.5C20.562,20.382,20.281,20.5,20,20.5z"></path><path d="M12,20.5c-0.282,0-0.562-0.118-0.76-0.35l-3-3.5c-0.321-0.374-0.321-0.927,0-1.301l3-3.5c0.36-0.419,0.992-0.467,1.41-0.108c0.419,0.359,0.468,0.991,0.108,1.41L10.317,16l2.442,2.85c0.359,0.419,0.311,1.05-0.108,1.409C12.462,20.421,12.231,20.5,12,20.5z"></path><path d="M14.251,23.5c-0.046,0-0.092-0.006-0.138-0.02c-0.266-0.075-0.419-0.353-0.344-0.618l4-14c0.075-0.266,0.349-0.419,0.618-0.344c0.266,0.076,0.419,0.353,0.343,0.618l-4,14C14.668,23.357,14.468,23.5,14.251,23.5z"></path></g></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!----><span ng-repeat="button in toolbarCtrl.primaryButtons">
    <!----><button ng-if="!button.isSeparator" type="button" ng-attr-id="{{::button.id}}" data-tid="more-button" ng-click="button.click($event)" ng-attr-track-outcome="{{::button.trackingOutcome}}" ng-attr-track-scenario="{{::button.trackingScenario}}" ng-attr-track-scenario-type="{{::button.trackingScenarioType}}" ng-attr-track-name="{{::button.trackingName}}" ng-attr-track-type="{{::button.trackingType}}" ng-attr-track-summary="{{::button.trackingSummary}}" ng-attr-track-data="toolbarCtrl.getTrackData(button)" ng-attr-data-prevent-refocus="{{::button.preventRefocus}}" ng-disabled="button.isDisabled" aria-label="Diğer seçenekler" title="Diğer seçenekler" class="compose-format-button ts-sym inset-border app-icons-fill-hover inset-border-themed icons-more app-icons-fill-focus inset-border-round " tabindex="-1" acc-role-dom="sub-menu-item" role="menuitem" track-outcome="4" track-scenario-type="36" track-type="23" track-summary="OverflowMenu" data-prevent-refocus="true">
      <!---->
      <!----><ng-include src="button.icon"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-more app-bar-extra-icons-fill-colors" focusable="false"><g class="icons-default-fill"><circle class="icons-filled" cx="22" cy="16" r="2"></circle><circle class="icons-filled" cx="16" cy="16" r="2"></circle><circle class="icons-filled" cx="10" cy="16" r="2"></circle><circle class="icons-unfilled" cx="22" cy="16" r="1.5"></circle><circle class="icons-unfilled" cx="16" cy="16" r="1.5"></circle><circle class="icons-unfilled" cx="10" cy="16" r="1.5"></circle></g></svg></ng-include>
    </button><!---->
    <!---->
  </span><!---->
</div></compose-format-toolbar>
            <!---->
            <!---->
            <!---->
          </div><!---->
          <!---->
          <div class="ts-editor-section">
            <div class="ts-compose-left-column">
              <!---->
              <!---->
              <div class="ts-edit-box" ng-click="nmCtrl.expandComposeOnClick()">
                <div class="ts-text-watermark" data-tid="textWatermark" ng-click="onPlaceholderClick($event)" aria-hidden="true">
                  Yeni bir mesaj yazın
                </div>
                <textarea class="ts-textarea-border ts-textarea-normal ckeditor-anchor" name="0f0a2fdc-1d79-4a6a-9400-21c3e0a4ca86" aria-hidden="true" id="0f0a2fdc-1d79-4a6a-9400-21c3e0a4ca86" style="visibility: hidden; display: none;"></textarea><div id="cke_0f0a2fdc-1d79-4a6a-9400-21c3e0a4ca86" class="cke_1 cke cke_reset cke_chrome cke_editor_0f0a2fdc-1d79-4a6a-9400-21c3e0a4ca86 cke_ltr cke_browser_webkit cke_hidpi" dir="ltr" lang="en" style="width: 100%;"><div class="cke_inner cke_reset" role="presentation"><span id="cke_1_top" class="cke_top cke_reset_all" role="presentation" style="height: auto; user-select: none;"><span id="cke_8" class="cke_voice_label">Editor toolbars</span><span id="cke_1_toolbox" class="cke_toolbox" role="group" aria-labelledby="cke_8" onmousedown="return false;"></span></span><div id="cke_1_contents" class="cke_contents cke_reset" role="presentation" style="height: 33px;"><div class="cke_wysiwyg_div cke_reset cke_enable_context_menu cke_editable cke_editable_themed cke_contents_ltr cke_show_borders" hidefocus="true" contenteditable="true" tabindex="0" spellcheck="true" role="textbox" aria-multiline="true" aria-label="Yeni bir ileti yazın, düzenleniyor" data-tid="ckeditor-newP2PMessage" kbshort-ignore="25,26"><div><br></div></div></div></div></div>
              </div>
            </div>
            <!---->
          </div>
        </div>
        <!---->
        <!---->
        <!----><div class="ts-extensions ts-full-width" ng-if="!nmCtrl.isInterop &amp;&amp; !nmCtrl.isLimitedChatExperience">
          <!---->
        </div><!---->
      </div>
    </form>
  </div>
  <!---->
  <!----><div class="extension-icons-container new-message-common compose-stripe" ng-if="!nmCtrl.isDisabledP2PChatWithBanner &amp;&amp; !nmCtrl.hideSendDiscard &amp;&amp; !nmCtrl.newMeetup &amp;&amp; !nmCtrl.disableComposeBox &amp;&amp; !nmCtrl.isConversationWithBlockedBot &amp;&amp; !nmCtrl.isConversationWithOneWayBot &amp;&amp; !nmCtrl.showCloseBtn" ng-class="{'compose-stripe-flex-reverse': nmCtrl.isInterop || nmCtrl.isLimitedChatExperience, 'extension-icons-container-editmessage': nmCtrl.isEditMessage, 'ts-disabled-input-extensions': nmCtrl.disableNewMessageAndInputExtensions || nmCtrl.isConversationArchived }" role="menu" prevent-override-role="true" data-tid="extension-icons" aria-label="Eylemler" acc-role-dom="menu tab-handler-new-message-extension-icons" kb-list="" kb-cyclic="">
    <!----><div class="clear-inline-block-padding compose-stripe" ng-if="!nmCtrl.isInterop &amp;&amp; !nmCtrl.isLimitedChatExperience &amp;&amp; !nmCtrl.hideInputExtensions" acc-role-dom="menu" kb-list="" kb-cyclic="" role="menu">
      <div class="extension-sub-icons compose-stripe" acc-role-dom="tab-handler-new-message-input-extension-icons">
        <div title="Biçimlendir">
          <button type="button" role="button" prevent-override-role="true" ng-class="{ 'selected': isExpanded }" tabindex="0" ng-disabled="nmCtrl.disableNewMessageAndInputExtensions || nmCtrl.isConversationArchived" ng-click="isExpanded ? collapse() : expand()" track-outcome="4" track-outcome-new="1" track-scenario="82" track-scenario-type="36" track-name="359" track-type="126" track-name-new="37" track-type-new="23" track-data="nmCtrl.getMessageMentions()" track-work-load="" track-sub-work-load="" track-summary="Expand compose box" class="extension-icon-button ts-sym app-icons-fill-hover app-icons-fill-focus inset-border inset-border-round inset-border-themed kb-active" ng-focus="nmCtrl.onFocusExpandCollapseButton()" ng-blur="nmCtrl.onBlurExpandCollapseButton()" aria-label="" data-tid="newMessageExpandButton" calling-screen-focus="expand-editor" acc-role-dom="menu-item" kb-item="">
                  <svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-format"><g class="icons-default-fill"><path class="icons-unfilled" d="M15.7022,19.7271l0.7853-0.7853L12.9724,8.8359c-0.0698-0.2012-0.2593-0.3359-0.4722-0.3359s-0.4023,0.1348-0.4722,0.3359
          l-4,11.4999c-0.0908,0.2607,0.0471,0.5454,0.3079,0.6362c0.262,0.0918,0.5459-0.0474,0.6365-0.3081l1.2745-3.664h4.5066
          L15.7022,19.7271z M10.5947,15.9999l1.9055-5.478l1.9055,5.478H10.5947z
          M23.5397,15.4603c-0.6143-0.6143-1.6147-0.6143-2.229,0l-4.5653,4.5653c-0.9816,0.1267-1.7452,0.9585-1.7452,1.9742
          c0,0.5513-0.4485,1-1,1h-2.5c-0.2761,0-0.5,0.2236-0.5,0.5s0.2239,0.5,0.5,0.5h5.5c1.0156,0,1.8475-0.7635,1.9742-1.7452
          l4.5653-4.5653c0.2969-0.2969,0.4604-0.6924,0.4604-1.1147C24.0001,16.1527,23.8365,15.7572,23.5397,15.4603z M17.0002,22.9998
          H15.722c0.1722-0.2953,0.2782-0.6341,0.2782-1c0-0.5513,0.4485-1,1-1s1,0.4487,1,1S17.5517,22.9998,17.0002,22.9998z
          M22.8327,16.9823l-4.0779,4.0779c-0.1863-0.3463-0.4687-0.6286-0.815-0.8149l4.0779-4.0779c0.2246-0.2241,0.5903-0.2246,0.8149,0
          c0.1082,0.1079,0.1675,0.2529,0.1675,0.4072C23.0001,16.7294,22.9408,16.8744,22.8327,16.9823z"></path><path class="icons-filled" d="M15.702,19.7271l0.7853-0.7853L12.9723,8.8359c-0.0698-0.2012-0.2593-0.3359-0.4722-0.3359s-0.4023,0.1348-0.4722,0.3359
                l-4,11.4999c-0.0908,0.2607,0.0471,0.5454,0.3079,0.6362c0.262,0.0918,0.5459-0.0474,0.6365-0.3081l1.2745-3.664h4.5066
                L15.702,19.7271z M10.5946,15.9999l1.9055-5.478l1.9055,5.478H10.5946z
          M23.5396,15.4603c-0.6143-0.6143-1.6147-0.6143-2.229,0l-3.5767,3.5767c1.0954,0.2715,1.9574,1.1336,2.229,2.229
                l3.5767-3.5767C23.8364,17.3924,24,16.9969,24,16.5746C24,16.1527,23.8364,15.7572,23.5396,15.4603z
          M17.0001,19.9998c-1.1028,0-2,0.897-2,2c0,0.5513-0.4485,1-1,1h-2.5c-0.2761,0-0.5,0.2236-0.5,0.5s0.2239,0.5,0.5,0.5h5.5
                c1.1028,0,2-0.897,2-2S18.1028,19.9998,17.0001,19.9998z"></path></g></svg>
          </button>
        </div>
      <!----><delivery-option ng-if="nmCtrl.enableDeliveryOption" importance="0" is-one-on-one-chat="nmCtrl.isOneOnOneChat" delivery-window="nmCtrl.priorityMessageDeliveryWindow" delivery-interval="nmCtrl.priorityMessageDeliveryInterval" format-command-source-id="new-message_78325826-0420-4114-bb28-9abe861bf6a4" custom-container-acc-role="tab-handler-new-message-compose-icons"><button type="button" role="button" data-tid="new-message-delivery-option-button" prevent-override-role="true" title="Teslim Seçeneklerini Ayarla" aria-label="Teslim seçeneklerini ayarlayın. Etkinleştirmek için Enter tuşuna, gezinmek için sol ok veya sağ ok tuşlarına basın." blur-on="click" ng-click="deliveryOptionCtrl.toggleTooltip($event, $root.resources.strings.icons_important, { templateUrl: 'components/message-delivery-option/message-delivery-option-popover.html', placement: 'top auto' })" class="ts-sym icons-redbang app-icons-fill-hover app-icons-fill-focus inset-border inset-border-round inset-border-themed" track-outcome="4" track-scenario="83" track-scenario-type="36" track-name="76" track-type="23" track-summary="Set delivery options" acc-role-dom="menu-item" kb-item="" tabindex="-1">
        <!----><ng-include src="'svg/icons-redbang.html'"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-redbang"><g class="icons-default-fill"><g class="icons-unfilled"><circle cx="16" cy="21.5" r="1"></circle><path d="M17.9806,11.2669l-0.9901,6.8805c-0.0781,0.5429-0.5847,0.9201-1.1315,0.8425c-0.4501-0.0638-0.7871-0.4171-0.8486-0.8425
            l-0.9901-6.8805c-0.1562-1.0857,0.6036-2.0916,1.6972-2.2467s2.1067,0.5993,2.263,1.685
            C18.0076,10.8931,18.0054,11.0879,17.9806,11.2669z"></path></g><g class="icons-filled"><circle cx="16" cy="21.5" r="1.5"></circle><path d="M18.4673,11.4246l-1.1419,6.9452c-0.121,0.7357-0.8122,1.2335-1.5438,1.1119c-0.5817-0.0967-1.0138-0.5581-1.1057-1.1119
            l-1.1148-6.7802c-0.2157-1.3119,0.525-2.6778,1.8126-3.0092c1.4407-0.3708,2.8565,0.5807,3.0938,2.0239
            C18.5126,10.88,18.5091,11.1632,18.4673,11.4246z"></path></g></g></svg></ng-include>
</button>
</delivery-option><!---->
        <!---->
        <!----><button type="button" role="button" prevent-override-role="true" title="Ekle" aria-label="Ekle. Gezinmek için sol ve sağ ok tuşlarını kullanın." ng-disabled="nmCtrl.disableNewMessageAndInputExtensions || nmCtrl.isConversationArchived" data-tid="select-attachment-button" ng-if="!nmCtrl.blockAttachments" ts-event-class="{ 'tooltip.show.before': 'selected', 'tooltip.hide.before': '-selected' }" class="ts-sym icons-attachment app-icons-fill-hover app-icons-fill-focus inset-border inset-border-round inset-border-themed" blur-on="click" tabindex="-1" data-prevent-refocus="false" ng-click="nmCtrl.addAttachment($event, this)" track-outcome="3" track-scenario="84" track-scenario-type="36" track-name="77" track-type="23" track-summary="Add attachment" acc-role-dom="menu-item" kb-item="">
          <svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-attachment"><g class="icons-default-fill"><path class="icons-unfilled" d="M20.7927,16.8364L16.021,21.554c-0.6099,0.6099-1.4224,0.9458-2.2876,0.9458s-1.6777-0.3359-2.2876-0.9458
                   c-1.2612-1.2615-1.2612-3.3137,0.0098-4.5852l6.7021-6.96c0.6567-0.6562,1.8059-0.6567,2.4622,0
                   c0.6787,0.679,0.6787,1.7832-0.0154,2.478l-5.7725,6.03c-0.1973,0.1931-0.2009,0.5098-0.0081,0.7073
                   c0.1936,0.1973,0.5098,0.2012,0.7073,0.0081l5.7957-6.0542c1.0688-1.0686,1.0688-2.8076,0-3.8762
                   c-0.5168-0.5171-1.2053-0.802-1.938-0.802s-1.4211,0.2849-1.9382,0.802l-6.7119,6.97c-1.6514,1.6511-1.6514,4.3381,0,5.9893
                   c0.8259,0.8259,1.9106,1.2388,2.9954,1.2388c1.084,0,2.1675-0.4124,2.9919-1.2368l4.7698-4.7156
                   c0.1963-0.1941,0.1982-0.5107,0.0039-0.707C21.3059,16.644,20.9893,16.6418,20.7927,16.8364z"></path><path class="icons-filled" d="M20.4412,16.4808l-4.7737,4.7197c-1.0664,1.0664-2.8018,1.0664-3.8682,0s-1.0664-2.8018,0.0195-3.8882l6.6924-6.95
                   c0.4678-0.4678,1.2874-0.4678,1.7551,0c0.4839,0.4839,0.4839,1.2712-0.0305,1.7869l-5.7532,6.0103
                   c-0.395,0.386-0.4021,1.019-0.0161,1.4141s1.019,0.4021,1.4141,0.0161c0,0,2.4329-2.3787,2.4453-2.3923l3.3545-3.6658
                   c1.2637-1.2637,1.2637-3.3196,0.0002-4.5833c-0.6116-0.6116-1.4255-0.9485-2.2917-0.9485s-1.6802,0.3369-2.2917,0.9485l-6.7119,6.97
                   c-1.8462,1.8462-1.8462,4.8501,0,6.6963c0.9236,0.9238,2.1367,1.3853,3.3496,1.3853c1.2114,0,2.4221-0.4607,3.3428-1.3811
                   l4.7698-4.7156c0.3926-0.3884,0.3962-1.0215,0.0081-1.4143C21.4673,16.0966,20.8342,16.0927,20.4412,16.4808z"></path></g></svg>
        </button><!---->
        <div oc-lazy-load="fun-stuff-picker">
          <!---->
          <!----><input-extension-emoji class="compose-stripe-directive" force-tooltip-below="false" ng-if="!nmCtrl.extendedSkypeEmoticons &amp;&amp; !nmCtrl.platformDetectService.isSurfaceHub() &amp;&amp; nmCtrl.enableNewComposeInputExtensions" ctrlid="funstuff_0f0a2fdc-1d79-4a6a-9400-21c3e0a4ca86" skype-conversation-id="nmCtrl.conversationId" is-disabled="nmCtrl.disableNewMessageAndInputExtensions || nmCtrl.isConversationArchived" message-type="nmCtrl.messageType" avoid-screen-edge="!!nmCtrl.messagePaneHost" data-prevent-refocus="true" set-refocus-callback="nmCtrl.funStuffPopoverHandler.setShouldRefocus(data)" data-tid="input-extension-emoji-button" team-name="nmCtrl.teamName"><!-- We need the high padding to prevent the popover overlaying on new-message area on non-expanded state.-->
<button type="button" role="button" prevent-override-role="true" class="ts-sym pull-right icons-emoji app-icons-fill-focus app-icons-fill-hover inset-border inset-border-round inset-border-themed shortcuts-funstuff" ng-disabled="emojiPicker.isDisabled" ng-click="emojiPicker.popoverMenuHandler($event, this)" data-prevent-refocus="false" track-outcome="1" track-scenario="87" track-scenario-type="36" track-name="79" track-type="23" track-summary="Emoji picker" ts-event-class="{ 'tooltip.show': 'selected', 'tooltip.hide': '-selected' }" data-tid="emojiPickerButton" title="Emoji" aria-label="Bir emoji seçin. Etkinleştirmek için Enter tuşuna, gezinmek için sol ok veya sağ ok tuşlarına basın." acc-role-dom="menu-item" kb-item="" tabindex="-1">
  <!----><ng-include src="'svg/icons-emoji.html'"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-emoji"><g class="icons-default-fill"><g class="icons-unfilled"><path d="M16,24c-4.4,0-8-3.6-8-8s3.6-8,8-8s8,3.6,8,8S20.4,24,16,24z M16,9c-3.9,0-7,3.1-7,7s3.1,7,7,7s7-3.1,7-7S19.9,9,16,9zM16,20.5c-1.4,0-2.8-0.5-3.9-1.6l0.7-0.7c1.8,1.8,4.6,1.8,6.4,0l0.7,0.7C18.9,19.9,17.4,20.5,16,20.5z"></path><circle cx="13" cy="15" r="1"></circle><circle cx="19" cy="15" r="1"></circle></g><path class="icons-filled" d="M24,16.734a7.069,7.069,0,0,1-.262,1.926A7.464,7.464,0,0,1,23,20.395,7.285,7.285,0,0,1,20.395,23a7.381,7.381,0,0,1-1.734.734A7.036,7.036,0,0,1,16.734,24H16.266a7.031,7.031,0,0,1-1.926-.262A7.381,7.381,0,0,1,12.605,23,7.285,7.285,0,0,1,10,20.395a7.4,7.4,0,0,1-.734-1.734A7.031,7.031,0,0,1,9,16.734V16.266a7.033,7.033,0,0,1,.262-1.926A7.4,7.4,0,0,1,10,12.605,7.285,7.285,0,0,1,12.605,10a7.443,7.443,0,0,1,1.734-.734A7.05,7.05,0,0,1,16.266,9h0.469a7.055,7.055,0,0,1,1.926.262A7.443,7.443,0,0,1,20.395,10,7.285,7.285,0,0,1,23,12.605a7.464,7.464,0,0,1,.734,1.734A7.071,7.071,0,0,1,24,16.266v0.469Zm-3.867,2.438-0.7-.7a4.154,4.154,0,0,1-5.859,0l-0.7.7a5.1,5.1,0,0,0,1.664,1.113,5.109,5.109,0,0,0,3.938,0A5.114,5.114,0,0,0,20.133,19.172ZM15,15a0.984,0.984,0,0,0-.078-0.387,1,1,0,0,0-.535-0.535,1,1,0,0,0-.773,0,1,1,0,0,0-.535.535,1,1,0,0,0,0,.773,1,1,0,0,0,.535.535,1,1,0,0,0,.773,0,1,1,0,0,0,.535-0.535A0.981,0.981,0,0,0,15,15Zm5,0a0.984,0.984,0,0,0-.078-0.387,1,1,0,0,0-.535-0.535,1,1,0,0,0-.773,0,1,1,0,0,0-.535.535,1,1,0,0,0,0,.773,1,1,0,0,0,.535.535,1,1,0,0,0,.773,0,1,1,0,0,0,.535-0.535A0.981,0.981,0,0,0,20,15Z"></path></g></svg></ng-include>
</button>
</input-extension-emoji><!---->
          <!----><input-extension-giphy class="compose-stripe-directive" force-tooltip-below="false" ng-if="!nmCtrl.platformDetectService.isSurfaceHub() &amp;&amp; nmCtrl.enableNewComposeInputExtensions &amp;&amp; nmCtrl.giphyEnabled" is-disabled="nmCtrl.disableNewMessageAndInputExtensions || nmCtrl.isConversationArchived" ctrlid="inputExtensionGiphy_0f0a2fdc-1d79-4a6a-9400-21c3e0a4ca86" skype-conversation-id="nmCtrl.conversationId" data-prevent-refocus="true" set-refocus-callback="nmCtrl.funStuffPopoverHandler.setShouldRefocus(data)" message-type="nmCtrl.messageType" avoid-screen-edge="!!nmCtrl.messagePaneHost" data-tid="input-extension-giphy-button" team-name="nmCtrl.teamName" team-id="nmCtrl.team.objectId" calling-screen-focus="fun-stuff-picker"><!-- We need the high padding to prevent the popover overlaying on new-message area on non-expanded state.-->
<button type="button" role="button" prevent-override-role="true" class="ts-sym pull-right icons-emoji app-icons-fill-focus app-icons-fill-hover inset-border inset-border-round inset-border-themed shortcuts-funstuff" ng-disabled="inputExtensionGiphy.isDisabled" ng-click="inputExtensionGiphy.popoverMenuHandler($event, this)" data-prevent-refocus="false" track-outcome="1" track-scenario="87" track-scenario-type="36" track-name="79" track-type="23" track-summary="Fun stuff picker" ts-event-class="{ 'tooltip.show': 'selected', 'tooltip.hide': '-selected' }" data-tid="inputExtensionGiphyPickerButton" title="Giphy" aria-label="Bir GIF seçin. Etkinleştirmek için Enter tuşuna, gezinmek için sol ok veya sağ ok tuşlarına basın." acc-role-dom="menu-item" kb-item="" tabindex="-1">
  <!----><ng-include src="'svg/icons-giphy.html'"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-emoji"><g class="icons-default-fill"><g class="icons-unfilled"><path d="M14.5,19h-1.7393c-1.0862,0-1.9668-0.8805-1.9668-1.9668v-1.858c0-1.2014,0.9739-2.1753,2.1753-2.1753H14.5v1h-1.5274
               c-0.651,0-1.1787,0.5277-1.1787,1.1787v1.8546c0,0.5345,0.4333,0.9668,0.9677,0.9668H13.5v-1.5H13v-1h1.5V19z"></path><rect x="16.0029" y="13" width="0.9971" height="6"></rect><polygon points="21.3467,14 21.3467,13 18.5,13 18.5,19 19.5029,19 19.5029,16.4824 21,16.4824 21,15.4824 19.5029,15.4824   19.5029,14 "></polygon><path d="M16,24c-2.0898,0-4.123-0.2109-6.043-0.6279C8.8232,23.125,8,22.0967,8,20.9258v-9.8521C8,9.9028,8.8232,8.874,9.957,8.6274
               c3.8418-0.833,8.2441-0.833,12.0859,0C23.1768,8.874,24,9.9028,24,11.0737v9.8521c0,1.1709-0.8232,2.1992-1.957,2.4463
               C20.123,23.7891,18.0898,24,16,24z M16,9.0005c-2.0176,0-3.9795,0.2036-5.8301,0.6055C9.4922,9.7529,9,10.3701,9,11.0737v9.8521
               c0,0.7031,0.4922,1.3203,1.1699,1.4678c3.6992,0.8047,7.9609,0.8047,11.6602,0C22.5078,22.2461,23,21.6289,23,20.9258v-9.8521
               c0-0.7036-0.4922-1.3208-1.1699-1.4678C19.9795,9.2041,18.0176,9.0005,16,9.0005z"></path></g><path class="icons-filled" d="M22.043,8.6274c-3.8418-0.833-8.2441-0.833-12.0859,0C8.8232,8.874,8,9.9028,8,11.0737v9.8521
                   c0,1.1709,0.8232,2.1992,1.957,2.4463C11.877,23.7891,13.9102,24,16,24s4.123-0.2109,6.043-0.6279
                   C23.1768,23.125,24,22.0967,24,20.9258v-9.8521C24,9.9028,23.1768,8.874,22.043,8.6274z M14.5,14h-1.5274
                   c-0.6509,0-1.1786,0.5277-1.1786,1.1786v1.8546c0,0.5345,0.4333,0.9668,0.9677,0.9668H13.5v-1.5H13v-1h1.5V19h-1.7393
                   c-1.0862,0-1.9667-0.8806-1.9667-1.9668v-1.858c0-1.2014,0.9739-2.1752,2.1752-2.1752H14.5V14z M17,19h-0.9971v-6H17V19z
                   M21.3467,14h-1.8438v1.4824H21v1h-1.4971V19H18.5v-6h2.8467V14z"></path></g></svg></ng-include>
</button>
</input-extension-giphy><!---->
          <!----><input-extension-stickers class="compose-stripe-directive" force-tooltip-below="false" ng-if="!nmCtrl.platformDetectService.isSurfaceHub() &amp;&amp; nmCtrl.enableNewComposeInputExtensions &amp;&amp; nmCtrl.stickersEnabled" ctrlid="inputExtensionStickers_0f0a2fdc-1d79-4a6a-9400-21c3e0a4ca86" is-disabled="nmCtrl.disableNewMessageAndInputExtensions || nmCtrl.isConversationArchived" skype-conversation-id="nmCtrl.conversationId" message-type="nmCtrl.messageType" avoid-screen-edge="!!nmCtrl.messagePaneHost" data-tid="input-extension-stickers-button" team-name="nmCtrl.teamName" data-prevent-refocus="true" set-refocus-callback="nmCtrl.funStuffPopoverHandler.setShouldRefocus(data)" on-save-callback="nmCtrl.funStuffPopoverHandler.saveMemeAndStickerCallback(data)" calling-screen-focus="fun-stuff-picker"><!-- We need the high padding to prevent the popover overlaying on new-message area on non-expanded state.-->
<button data-placement="auto center" type="button" role="button" prevent-override-role="true" class="ts-sym pull-right icons-emoji app-icons-fill-focus app-icons-fill-hover inset-border inset-border-round inset-border-themed shortcuts-funstuff" ng-disabled="inputExtensionStickers.isDisabled" ng-click="inputExtensionStickers.popoverMenuHandler($event, this)" data-prevent-refocus="false" track-outcome="1" track-scenario="87" track-scenario-type="36" track-name="79" track-type="23" track-summary="Stickers input Extension picker" ts-event-class="{ 'tooltip.show': 'selected', 'tooltip.hide': '-selected' }" data-tid="inputExtensionStickersButton" title="Çıkartma" aria-label="Bir etiket seçin. Etkinleştirmek için Enter tuşuna, gezinmek için sol ok veya sağ ok tuşlarına basın." acc-role-dom="menu-item" kb-item="" tabindex="-1">
  <!----><ng-include src="'svg/icons-sticker.html'"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-emoji"><g class="icons-default-fill"><g class="icons-unfilled"><path d="M14.793,14.011c0,0.1045-0.0225,0.2046-0.0664,0.3008c-0.0449,0.0967-0.1035,0.1812-0.1758,0.2539
                     c-0.0732,0.0732-0.1582,0.1318-0.2539,0.1758c-0.0967,0.0444-0.1973,0.0664-0.3008,0.0664c-0.1045,0-0.2051-0.022-0.3008-0.0664
                     c-0.0967-0.0439-0.1816-0.1025-0.2539-0.1758c-0.0732-0.0728-0.1318-0.1572-0.1758-0.2539
                     c-0.0449-0.0962-0.0664-0.1963-0.0664-0.3008c0-0.104,0.0215-0.2041,0.0664-0.3008c0.0439-0.0962,0.1025-0.1821,0.1758-0.2578
                     c0.0723-0.0752,0.1572-0.1353,0.2539-0.1797c0.0957-0.0439,0.1963-0.0664,0.3008-0.0664c0.1035,0,0.2041,0.0225,0.3008,0.0664
                     c0.0957,0.0444,0.1807,0.1045,0.2539,0.1797c0.0723,0.0757,0.1309,0.1616,0.1758,0.2578
                     C14.7705,13.8069,14.793,13.907,14.793,14.011z"></path><path d="M18.793,14.011c0,0.1045-0.0225,0.2046-0.0664,0.3008c-0.0439,0.0967-0.1025,0.1812-0.1758,0.2539
                     c-0.0732,0.0732-0.1572,0.1318-0.2539,0.1758c-0.0967,0.0444-0.1963,0.0664-0.3008,0.0664s-0.2041-0.022-0.3008-0.0664
                     c-0.0967-0.0439-0.1807-0.1025-0.2539-0.1758c-0.0732-0.0728-0.1318-0.1572-0.1758-0.2539
                     c-0.0439-0.0962-0.0664-0.1963-0.0664-0.3008c0-0.104,0.0225-0.2041,0.0664-0.3008c0.0439-0.0962,0.1025-0.1821,0.1758-0.2578
                     c0.0732-0.0752,0.1572-0.1353,0.2539-0.1797c0.0967-0.0439,0.1963-0.0664,0.3008-0.0664s0.2041,0.0225,0.3008,0.0664
                     c0.0967,0.0444,0.1807,0.1045,0.2539,0.1797c0.0732,0.0757,0.1318,0.1616,0.1758,0.2578
                     C18.7705,13.8069,18.793,13.907,18.793,14.011z"></path><path d="M21.5,9h-11C9.6729,9,9,9.6729,9,10.5v11c0,0.8271,0.6729,1.5,1.5,1.5h6.5859c0.3945,0,0.7812-0.1602,1.0605-0.4395
                     l4.4141-4.4141C22.8398,17.8672,23,17.4805,23,17.0859V10.5C23,9.6729,22.3271,9,21.5,9z M10,21.5v-11c0-0.2759,0.2241-0.5,0.5-0.5
                     h11c0.2754,0,0.5,0.2241,0.5,0.5V17h-5v1.3505c-0.3055,0.0933-0.6393,0.1423-1.0039,0.1423c-0.3809,0-0.7256-0.0498-1.0352-0.1484
                     c-0.3105-0.0986-0.5918-0.2236-0.8438-0.375c-0.2529-0.1514-0.4795-0.3135-0.6797-0.4883
                     c-0.2012-0.1748-0.3789-0.3369-0.5352-0.4883s-0.293-0.2764-0.4102-0.375s-0.2207-0.1484-0.3086-0.1484
                     c-0.0781,0-0.1543,0.0171-0.2266,0.0508c-0.0732,0.0342-0.1367,0.0781-0.1914,0.1328s-0.0977,0.1182-0.1289,0.1914
                     s-0.0469,0.1484-0.0469,0.2266c0,0.0625,0.0098,0.1211,0.0312,0.1758c0.0205,0.0547,0.0439,0.1084,0.0703,0.1602
                     c0.1924,0.3594,0.4512,0.6797,0.7773,0.9609c0.3252,0.2812,0.6846,0.5205,1.0781,0.7188c0.3926,0.1982,0.8018,0.3486,1.2266,0.4531
                     c0.4238,0.1045,0.832,0.1562,1.2227,0.1562c0.3221,0,0.6586-0.0442,1.0039-0.1151V22h-6.5C10.2241,22,10,21.7754,10,21.5z
                     M18,21.293v-2.0128V18h3.293L18,21.293z"></path></g><g class="icons-filled"><path d="M17,19.5807c-0.3453,0.0709-0.6818,0.1151-1.0039,0.1151c-0.3906,0-0.7988-0.0518-1.2227-0.1562
                     c-0.4248-0.1045-0.834-0.2549-1.2266-0.4531c-0.3936-0.1982-0.7529-0.4375-1.0781-0.7188c-0.3262-0.2812-0.585-0.6016-0.7773-0.9609
                     c-0.0264-0.0518-0.0498-0.1055-0.0703-0.1602c-0.0215-0.0547-0.0312-0.1133-0.0312-0.1758c0-0.0781,0.0156-0.1533,0.0469-0.2266
                     s0.0742-0.1367,0.1289-0.1914s0.1182-0.0986,0.1914-0.1328c0.0723-0.0337,0.1484-0.0508,0.2266-0.0508
                     c0.0879,0,0.1914,0.0498,0.3086,0.1484s0.2539,0.2236,0.4102,0.375s0.334,0.3135,0.5352,0.4883
                     c0.2002,0.1748,0.4268,0.3369,0.6797,0.4883c0.252,0.1514,0.5332,0.2764,0.8438,0.375c0.3096,0.0986,0.6543,0.1484,1.0352,0.1484
                     c0.3646,0,0.6984-0.049,1.0039-0.1423V17h6v-6.5C23,9.6729,22.3271,9,21.5,9h-11C9.6729,9,9,9.6729,9,10.5v11
                     c0,0.8271,0.6729,1.5,1.5,1.5H17V19.5807z M17.2656,13.7102c0.0439-0.0962,0.1025-0.1821,0.1758-0.2578
                     c0.0732-0.0752,0.1572-0.1353,0.2539-0.1797c0.0967-0.0439,0.1963-0.0664,0.3008-0.0664s0.2041,0.0225,0.3008,0.0664
                     c0.0967,0.0444,0.1807,0.1045,0.2539,0.1797c0.0732,0.0757,0.1318,0.1616,0.1758,0.2578c0.0439,0.0967,0.0664,0.1968,0.0664,0.3008
                     c0,0.1045-0.0225,0.2046-0.0664,0.3008c-0.0439,0.0967-0.1025,0.1812-0.1758,0.2539c-0.0732,0.0732-0.1572,0.1318-0.2539,0.1758
                     c-0.0967,0.0444-0.1963,0.0664-0.3008,0.0664s-0.2041-0.022-0.3008-0.0664c-0.0967-0.0439-0.1807-0.1025-0.2539-0.1758
                     c-0.0732-0.0728-0.1318-0.1572-0.1758-0.2539c-0.0439-0.0962-0.0664-0.1963-0.0664-0.3008
                     C17.1992,13.907,17.2217,13.8069,17.2656,13.7102z M13.2656,13.7102c0.0439-0.0962,0.1025-0.1821,0.1758-0.2578
                     c0.0723-0.0752,0.1572-0.1353,0.2539-0.1797c0.0957-0.0439,0.1963-0.0664,0.3008-0.0664c0.1035,0,0.2041,0.0225,0.3008,0.0664
                     c0.0957,0.0444,0.1807,0.1045,0.2539,0.1797c0.0723,0.0757,0.1309,0.1616,0.1758,0.2578c0.0439,0.0967,0.0664,0.1968,0.0664,0.3008
                     c0,0.1045-0.0225,0.2046-0.0664,0.3008c-0.0449,0.0967-0.1035,0.1812-0.1758,0.2539c-0.0732,0.0732-0.1582,0.1318-0.2539,0.1758
                     c-0.0967,0.0444-0.1973,0.0664-0.3008,0.0664c-0.1045,0-0.2051-0.022-0.3008-0.0664c-0.0967-0.0439-0.1816-0.1025-0.2539-0.1758
                     c-0.0732-0.0728-0.1318-0.1572-0.1758-0.2539c-0.0449-0.0962-0.0664-0.1963-0.0664-0.3008
                     C13.1992,13.907,13.2207,13.8069,13.2656,13.7102z"></path><path d="M18,18v1.2802v3.4001c0.05-0.0385,0.1016-0.075,0.1465-0.1198l4.4141-4.4141C22.6054,18.1016,22.6418,18.05,22.6804,18H18z"></path></g></g></svg></ng-include>
</button>
</input-extension-stickers><!---->
        </div>

        <!---->
        <!---->
        <!----><input-extensions-selector class="compose-stripe" ng-if="!nmCtrl.platformDetectService.isSurfaceHub() &amp;&amp; nmCtrl.enableNewFullInputExtensions &amp;&amp; nmCtrl.showInputExtensionsSelector" recalculate-compose-extension="nmCtrl.recalculateComposeExtension" ctrlid="funstuff_0f0a2fdc-1d79-4a6a-9400-21c3e0a4ca86" skype-conversation-id="nmCtrl.conversationId" reply-chain-id="" data-prevent-refocus="true" is-disabled="nmCtrl.disableNewMessageAndInputExtensions || nmCtrl.isConversationArchived" message-type="nmCtrl.messageType" avoid-screen-edge="!!nmCtrl.messagePaneHost" data-tid="input-extension-list-button" is-conv-id-unavailable="nmCtrl.isConvIdUnavailable"><div class="input-extensions-inline-pinned compose-stripe" data-tid="composeExtensionPinned" ng-class="{'disable-input-extensions': ctrl.isDisabled}">
  <!----><ul class="input-extensions-inline-pinned" ng-if="ctrl.enablePinningComposeExtensions" role="none">
    <!----><li class="input-extensions-inline-pinned-item" ng-repeat="item in ctrl.favoritesVisible track by $index" role="none">
      <button class="ts-sym icons-emoji app-icons-fill-hover shortcuts-funstuff inset-border inset-border-round inset-border-themed" prevent-override-role="true" ts-event-class="{ 'tooltip.show': 'selected', 'tooltip.hide': '-selected' }" ng-disabled="ctrl.isDisabled" ng-click="ctrl.onInputExtensionClicked($event, item, true)" data-prevent-refocus="false" data-tid="composePinnedItems" title="Takdir" aria-label="Takdir" role="button" aria-setsize="6" aria-posinset="4" ts-right-click="ctrl.contextMenuHandler($event, this, item)" track-click-silent="true" acc-role-dom="menu-item" kb-item="" tabindex="-1">
        <div class="fav-image-container">
          <!---->
          <!----><svg ng-if="::!ctrl.utilityService.useNgIncludeForIcon(item.imageUrlSmall)" class="input-extensions-img input-extensions-svg">
            <filter ng-attr-id="input-extension-filter-{{ctrl.favoritesVisibleIconId[ $index ]}}" id="input-extension-filter-7420398c46894fd684c6f03ccc4914f4">
              <feColorMatrix color-interpolation-filters="sRGB" in="SourceGraphic" type="matrix" ng-attr-values="{{::ctrl.svgImageColorFilterMatrixValue()}}" values="0.08627450980392157  0           0           0           0
    0           0.13725490196078433  0           0           0
    0           0           0.22745098039215686  0           0
    0           0           0           0.74  0">
              </feColorMatrix>
            </filter>
            <image ng-attr-filter="url(#input-extension-filter-{{ctrl.favoritesVisibleIconId[ $index ]}})" xlink:href="https://statics.teams.cdn.office.net/evergreen-assets/apps/d832a33f-28c2-4969-8ad0-4fee681dc5b4_smallImage.png?v=1.0.20200917" ng-attr-xlink:href="{{ctrl.getSvgImageXlinkHref(item)}}" width="100%" height="100%" filter="url(#input-extension-filter-7420398c46894fd684c6f03ccc4914f4)">
            </image>
          </svg><!---->
        </div>
      </button>
    </li><!----><li class="input-extensions-inline-pinned-item" ng-repeat="item in ctrl.favoritesVisible track by $index" role="none">
      <button class="ts-sym icons-emoji app-icons-fill-hover shortcuts-funstuff inset-border inset-border-round inset-border-themed" prevent-override-role="true" ts-event-class="{ 'tooltip.show': 'selected', 'tooltip.hide': '-selected' }" ng-disabled="ctrl.isDisabled" ng-click="ctrl.onInputExtensionClicked($event, item, true)" data-prevent-refocus="false" data-tid="composePinnedItems" title="Onaylar" aria-label="Onaylar" role="button" aria-setsize="6" aria-posinset="5" ts-right-click="ctrl.contextMenuHandler($event, this, item)" track-click-silent="true" acc-role-dom="menu-item" kb-item="" tabindex="-1">
        <div class="fav-image-container">
          <!---->
          <!----><svg ng-if="::!ctrl.utilityService.useNgIncludeForIcon(item.imageUrlSmall)" class="input-extensions-img input-extensions-svg">
            <filter ng-attr-id="input-extension-filter-{{ctrl.favoritesVisibleIconId[ $index ]}}" id="input-extension-filter-dfc3ce7b8538485c81cd99d22bd937c5">
              <feColorMatrix color-interpolation-filters="sRGB" in="SourceGraphic" type="matrix" ng-attr-values="{{::ctrl.svgImageColorFilterMatrixValue()}}" values="0.08627450980392157  0           0           0           0
    0           0.13725490196078433  0           0           0
    0           0           0.22745098039215686  0           0
    0           0           0           0.74  0">
              </feColorMatrix>
            </filter>
            <image ng-attr-filter="url(#input-extension-filter-{{ctrl.favoritesVisibleIconId[ $index ]}})" xlink:href="https://statics.teams.cdn.office.net/evergreen-assets/apps/approvals_smallimage.png" ng-attr-xlink:href="{{ctrl.getSvgImageXlinkHref(item)}}" width="100%" height="100%" filter="url(#input-extension-filter-dfc3ce7b8538485c81cd99d22bd937c5)">
            </image>
          </svg><!---->
        </div>
      </button>
    </li><!---->
  </ul><!---->
  <!-- We need the high padding to prevent the popover overlaying on new-message area on non-expanded state.-->
  <!----><button type="button" role="button" aria-setsize="6" aria-posinset="6" prevent-override-role="true" class="ts-sym pull-right icons-emoji app-icons-fill-hover shortcuts-funstuff inset-border inset-border-round inset-border-themed showmore-options" ng-disabled="ctrl.isDisabled" ng-if="ctrl.shouldShowMoreOptions" ng-click="ctrl.showMoreOptions($event)" data-prevent-refocus="false" track-outcome="1" track-scenario="762" track-scenario-type="36" track-name="79" track-type="23" track-summary="list selector picker" ts-event-class="{ 'tooltip.show': 'selected', 'tooltip.hide': '-selected' }" data-tid="inputExtensionsSelectorPickerButton" title="İleti uzantıları" aria-label="İleti uzantıları" acc-role-dom="menu-item" kb-item="" tabindex="-1">
    <!----><ng-include src="'svg/icons-more.html'"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-more app-bar-extra-icons-fill-colors" focusable="false"><g class="icons-default-fill"><circle class="icons-filled" cx="22" cy="16" r="2"></circle><circle class="icons-filled" cx="16" cy="16" r="2"></circle><circle class="icons-filled" cx="10" cy="16" r="2"></circle><circle class="icons-unfilled" cx="22" cy="16" r="1.5"></circle><circle class="icons-unfilled" cx="16" cy="16" r="1.5"></circle><circle class="icons-unfilled" cx="10" cy="16" r="1.5"></circle></g></svg></ng-include>
  </button><!---->
</div>
</input-extensions-selector><!---->
      </div>
    </div><!---->
    <div class="compose-send-discard" acc-role-dom="tab-handler-new-send-discard-buttons">
      <!---->
      <!----><button id="send-message-button" type="button" ng-if="!nmCtrl.isDisabledP2PChatWithBanner" ng-click="nmCtrl.send()" ng-disabled="nmCtrl.disableNewMessageAndInputExtensions || nmCtrl.isConversationArchived || nmCtrl.disableSendTillAllFilesCreated" ng-class="{'disable-send-button' : nmCtrl.disableSendTillAllFilesCreated}" ng-attr-calling-screen-focus="{{::(nmCtrl.isCallingScreen) ? 'calling-chat-exit-point' : undefined}}" role="button" prevent-override-role="true" tabindex="-1" class="extension-icon-button focus-round-border ts-sym pull-left app-icons-fill-hover icons-send inset-border inset-border-round inset-border-themed compose-stripe-directive" ng-attr-title="{{nmCtrl.disableSendTillAllFilesCreated ? nmCtrl.translatedLabelsMap[$root.resources.strings.icons_sendButtonDisabled_Async] : nmCtrl.sendMessageBtnTitle}}" ng-attr-aria-label="{{nmCtrl.disableSendTillAllFilesCreated ? nmCtrl.translatedLabelsMap[$root.resources.strings.icons_sendButtonDisabled_Async] : nmCtrl.translatedLabelsMap[$root.resources.strings.icons_send_arialabel]}}" track-click-silent="true" data-tid="messageComposeButtonSend" title="Gönder" aria-label="Gönder">
        <!----><ng-include src="nmCtrl.isEditMessage ? 'svg/icons-accept.html' : 'svg/icons-send.html'"><svg viewBox="0 0 32 32" role="presentation" class="app-svg icons-send icons-rtl-flip"><g class="icons-default-fill"><path class="icons-unfilled" d="M23,15.6C23,15.6,23,15.6,23,15.6L9.4,10.1C9.1,9.9,8.7,10,8.4,10.2c-0.3,0.2-0.4,0.6-0.3,1l1.2,5.3L8,21.8
          c-0.1,0.4,0,0.7,0.3,1C8.6,22.9,8.8,23,9,23c0.1,0,0.3,0,0.4-0.1L23,17.4c0.4-0.2,0.6-0.5,0.6-0.9C23.6,16.1,23.4,15.8,23,15.6z
          M9,11l12.3,5H10.2L9,11z M9,22l1.2-5h11.2L9,22z"></path><path class="icons-filled" d="M23.2074,15.0927c-0.0063-0.0029-0.0127-0.0056-0.0193-0.0083L9.6355,9.4773c-0.3496-0.1626-0.7519-0.1128-1.051,0.1301
                c-0.2991,0.2424-0.4311,0.6262-0.3447,1.0017l1.1287,4.8908h10.1314v1H9.3685L8.2398,21.391
                c-0.0864,0.3752,0.0457,0.759,0.3447,1.0015c0.1851,0.1501,0.4097,0.2263,0.6323,0.2263c0.137,0,0.2734-0.0291,0.3992-0.0876
                l13.5915-5.624c0.3572-0.166,0.5791-0.5134,0.5791-0.9072C23.7865,15.6061,23.5646,15.2587,23.2074,15.0927z"></path></g></svg></ng-include>
      </button><!---->
    </div>
  </div><!---->
</div></new-message><!---->
      <!---->
      <!---->
    </div>
    <!---->
  </div>
</message-pane></div><!----></div></messages-header><!----><!----><!----></div></div><!----><broadcast-playback-monitor ng-class="{'full-page': app.layoutService.isBroadcastPlayback }"><!----></broadcast-playback-monitor><!----><div class="ts-draggable-multi-call-list-container ng-hide" ng-if="::ctrl.enableFloatingCallMonitor" ng-show="ctrl.shouldShow()" ng-class="{'one-call': ctrl.hasOnlyOneCall, 'vdi-enabled': ctrl.useVDIUX}">
  <div class="ts-draggable-multi-call-list-header">
    <div class="icon-float-center">
      <!----><ng-include class="icons-white-override" src="'svg/icons-gripper.html'" aria-hidden="true"><svg viewBox="0 0 18 18" class="app-svg icons-gripper"><g><circle cx="9" cy="5.6" r="2.3"></circle><circle cx="9" cy="12.4" r="2.3"></circle><circle cx="15.7" cy="5.6" r="2.3"></circle><circle cx="15.7" cy="12.4" r="2.3"></circle><circle cx="2.3" cy="5.6" r="2.3"></circle><circle cx="2.3" cy="12.4" r="2.3"></circle></g></svg></ng-include>
    </div>
  </div>
  <multi-call-list context="floating_call_monitor"><!----><!----></multi-call-list>
</div><!----></div><!----><div analytics-panel="2" context-view-component="right"><!----></div></div><div class="acc-hidden-element"><span id="accessibility-help-element" tabindex="-1" aria-label=""></span></div></div><!----><!----><!----><promote-desktop><!----></promote-desktop><!----><promote-mobile ng-if="app.layoutService.isLoaded"><!----></promote-mobile><!----><script nonce="">sendAppStateChanged("IndexHtmlLoaded");</script><div id="aria-live-assertive" aria-atomic="true" aria-live="assertive"></div><div id="aria-live-polite" aria-atomic="true" aria-live="polite"></div><div style="width: 200px; height: 200px; position: absolute; top: -9999px; overflow: scroll;"></div></body></html>"""
