/*Create a Tab view object*/
lv_obj_t *tabview;
tabview = lv_tabview_create(lv_scr_act(), NULL);

/*Add 3 tabs (the tabs are page (lv_page) and can be scrolled*/
lv_obj_t *tab1 = lv_tabview_add_tab(tabview, "Tab 1");
lv_obj_t *tab2 = lv_tabview_add_tab(tabview, "Tab 2");
lv_obj_t *tab3 = lv_tabview_add_tab(tabview, "Tab 3");


/*Add content to the tabs*/
lv_obj_t * label = lv_label_create(tab1, NULL);
lv_label_set_text(label, "This the first tab\n\n"
                         "If the content\n"
                         "become too long\n"
                         "the tab become\n"
                         "scrollable\n\n");

label = lv_label_create(tab2, NULL);
lv_label_set_text(label, "Second tab");

label = lv_label_create(tab3, NULL);
lv_label_set_text(label, "Third tab");