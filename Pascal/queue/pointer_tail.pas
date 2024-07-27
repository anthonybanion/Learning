{@brief Implementasi queue dengan pointer
 @file pointer_tail.pas
 @date 06/01/2024
 @version 1.0}
program pointer_tail;
{$T+}
type
age_number  = byte;
node_linker = ^Tnodo;

Tnodo = record
    data : age_number;
    next : node_linker;
end;

Tqueue = record
    head : node_linker;
    tail : node_linker;
end;

procedure create_queue(var queue : Tqueue);
begin
    queue.head := nil;
    queue.tail := nil;
end;

function is_empty(queue : Tqueue): Boolean;
begin
    is_empty := (queue.head = nil) and (queue.tail = nil);
end;

procedure enqueue(var queue : Tqueue; data : age_number);
var
    new_node : node_linker;
begin
    new(new_node);
    new_node^.data := data;
    new_node^.next := nil;
    if is_empty(queue) then
    begin
        queue.head := new_node;
        queue.tail := new_node;
    end
    else
    begin
        queue.tail^.next := new_node;
        queue.tail := new_node;
    end;
end;

procedure read_front(queue : Tqueue; var data : age_number; var is_successful : Boolean);
begin
    if is_empty(queue) then
    begin
        is_successful := false;
    end
    else
    begin
        is_successful := true;
        data := queue.head^.data;
    end;
end;

procedure delete_data(var queue : Tqueue; var is_successful : Boolean);
var
    auxiliary : node_linker;
begin
    if is_empty(queue) then
    begin
        is_successful := false;
    end
    else
    begin
        is_successful := true;
        auxiliary := queue.head;
        queue.head := queue.head^.next;
        dispose(auxiliary);
    end;
end;

var
    queue           : Tqueue;
    is_successful   : Boolean;
    data            : age_number;
    i               : byte;

begin
    create_queue(queue);
    for i := 34 to 52 do
    enqueue(queue, i);

    while not is_empty(queue) do
    begin
        read_front(queue, data, is_successful);
        if is_successful then
        begin
            writeln('Data : ', data);
           delete_data(queue, is_successful);
        end;
    end;
    dispose(queue.head);
    dispose(queue.tail);
end.
