{* @brief CRUD operations on a linked_list.
 * @details This program implements CRUD operations on a linked_list.
 * @file crud_linked_list.pas
 * @date 05/01/2014
 * @version 1.0}
Program crud_linked_list;
type
  node_linker = ^node;
  node = record
    data: integer;
    next: node_linker;
  end;

procedure initialize_list(var head, tail : node_linker);
begin
    new(head);
    head^.data := 0;
    tail := head;
end;

procedure interface_menu;
begin
    writeln('1. Insert');
    writeln('2. Delete');
    writeln('3. Update');
    writeln('4. Search');
    writeln('5. Print');
    writeln('6. Exit');
    write('Enter your choice: ');
end;

procedure insert_node(var head, tail : node_linker);
var
    auxiliary: node_linker;
    data: integer;
begin
    new(auxiliary);
    write('Enter data: ');
    readln(data);
    auxiliary^.data := data;
    tail^.next := auxiliary;
    tail := auxiliary;
    tail^.next := nil;
end;

procedure delete_node(var head, tail : node_linker);
var
    auxiliary: node_linker;
    data: integer;
begin    
    write('Enter data: ');
    readln(data);
    auxiliary := head;
    while (auxiliary <> nil) and (auxiliary^.data <> data) do
        auxiliary := auxiliary^.next;
    if auxiliary <> nil then
    begin
        if auxiliary = tail then
            tail := tail^.next;
        auxiliary^.data := auxiliary^.next^.data;
        auxiliary^.next := auxiliary^.next^.next;
    end;
end;

procedure update_node(var head, tail : node_linker);
var
    auxiliary: node_linker;
    data: integer;
begin    
    write('Enter data: ');
    readln(data);
    auxiliary := head;
    while (auxiliary <> nil) and (auxiliary^.data <> data) do
        auxiliary := auxiliary^.next;
    if auxiliary <> nil then
    begin
        write('Enter new data: ');
        readln(auxiliary^.data);
    end;
end;
procedure print_list(head : node_linker);
begin
    while head <> nil do
    begin
        writeln(head^.data);
        head := head^.next;
    end;

end;
procedure search_node(var head, tail : node_linker);
var
    auxiliary: node_linker;
    data: integer;
begin   
    write('Enter data: ');
    readln(data);
    auxiliary := head;
    while (auxiliary <> nil) and (auxiliary^.data <> data) do
        auxiliary := auxiliary^.next;
    if auxiliary <> nil then
        writeln('Data found: ', auxiliary^.data)
    else
        writeln('Data not found');
end;

var
    head: node_linker;
    tail: node_linker;
    response: integer;
begin

    initialize_list(head, tail);

    repeat
    interface_menu;
    readln(response);

    case response of
        1: insert_node(head, tail);
        2: delete_node(head, tail);
        3: update_node(head, tail);
        4: search_node(head, tail);
        5: print_list(head); 
    end;
    until response = 6;
    
    Dispose(head);
    Dispose(tail);

end.