/**
 * 
 * This class represents a library item with a title, 
 * author, item ID, and type.
 * 
 * File: LibraryItem.java
 * Author: Anthony Bañon
 * Created: 2025-05-24
 * Last Updated: 2025-05-24
 */



package paradigm_oop.generics;
// Generic LibraryItem class to store information about any type of library item
public class LibraryItem<T> {
    private String title;
    private String author;
    private String itemID;
    private T itemType;

    public LibraryItem(String title, String author, String itemID, T itemType) {
        this.title = title;
        this.author = author;
        this.itemID = itemID;
        this.itemType = itemType;
    }

    public String getItemID() {
        return itemID;
    }

    @Override
    public String toString() {
        return "Item ID: " + itemID + "\nTitle: " + title + "\nAuthor: " + author + "\nType: " + itemType + "\n";
    }
}
